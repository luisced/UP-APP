from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from school import db
from school.tools.utils import color
from school.models import ChromeBrowser, Subject, Student
from school.relations import RelationStudentSubjectTable
from school.student.utils import createStudentSubjectRelationship, getStudent
from datetime import datetime
from flask import session
import re
import traceback
import logging
import time


def findScheduleTable(browser):
    try:
        scheduleContent = browser.find_element(By.ID, "contenido-tabla")
        logging.info(f'{color(2,"Schedule content found")} ✅')
    except NoSuchElementException:
        logging.error(f'{color(1,"Schedule content not found")} ❌')
    return scheduleContent


def findScheduleSubjects(scheduleContent: str) -> list[str]:
    '''Extracts the schedule subjects from the schedule content'''
    try:
        rows = scheduleContent.find_elements(By.CSS_SELECTOR, "div.row")
        logging.info(f'{color(4,f"Schedule content has {len(rows)} rows")}🔎')
    except NoSuchElementException:
        logging.warning(f'{color(1,"Schedule content has no rows")} ❌')

    data = []
    for row in rows:
        # Find all the div elements within the row
        cells = row.find_elements(By.CSS_SELECTOR, 'div')

        # Extract the data from the cells
        cell_data = [cell.text for cell in cells]

        # Add the data to the list
        data.append(cell_data)

    return data


def cleanScheduleData(subjectsList: list[list[Subject]]) -> list[dict[str, str]]:
    '''Cleans the schedule data'''
    cleanedSubjects = []
    for subjectData in subjectsList:
        # Create a dictionary with all subject data
        subject_data = {
            'day': subjectData[1].strip(),
            'start_time': subjectData[2].strip(),
            'end_time': subjectData[3].strip(),
            'subject': subjectData[4].strip(),
            'teacher': subjectData[6].strip(),
            'start_date': subjectData[7].strip(),
            'end_date': subjectData[8].strip(),
            'group': subjectData[9].strip(),
            'classroom': re.compile(
                r'([^/]*)$').search(re.sub(r'\n', '', subjectData[5].strip())).group(1).replace('Ver', '').lstrip()
        }

        # Add the subject data to the list
        cleanedSubjects.append(subject_data)

    return cleanedSubjects


def loadScheduleData(scheduleSubjects: list[dict[str, str]]) -> list[dict[str, str]]:
    '''Loads the schedule data into a Subject object'''
    current_day = ''
    subjects = [subject for subject in scheduleSubjects if subject != []]
    try:
        subject_data = cleanScheduleData(subjects)
        for data in subject_data:
            data['day'] = data['day'] if data['day'] else current_day
            subject = createSubject(**data)
            createStudentSubjectRelationship(Student.query.filter_by(
                studentID=session['student']['studentID']).first(), subject)
            current_day = data['day']
        logging.info(f'{color(4,"Schedule data loaded into DB")} ✅')
    except Exception as e:
        logging.error(
            f'{color(1,"Schedule data not loaded into DB")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
        subject_data = None
    return subject_data


def createSubject(day: str, start_time: datetime, end_time: datetime, subject: str, teacher: str, start_date: datetime, end_date: datetime, group: str, classroom: str):
    '''Creates a subject object'''
    try:

        if not Subject.query.filter_by(group=group, day=day).first():
            subject = Subject(day=day, startTime=start_time, endTime=end_time, name=subject, teacher=teacher,
                              startDate=datetime.strptime(start_date, '%d/%m/%Y'), endDate=datetime.strptime(end_date, '%d/%m/%Y'), group=group, classroom=classroom)
            db.session.add(subject)
            db.session.commit()
            logging.info(f"{color(2,'Subject created:')} ✅")
        else:
            raise ValueError(
                f"{color(3,'Subject already exists in the database')}")
    except Exception as e:
        logging.error(
            f"{color(1,'Subject not created')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
        subject = None
    return subject


def getSubject(subject: Subject) -> dict[str, str]:
    '''Returns the subject data as a dictionary'''
    subjects = Subject.to_dict(Subject.query.filter_by(id=subject.id).first())
    logging.info(f"{color(2,'Get Subject Complete')} ✅")
    return formatDateObjsSubject(subjects)


def getStudentSubjects(student: Student) -> dict:
    '''Returns the student subjects as a dictionary with his subjects'''
    try:
        subjectIDs = [subject.id for subject in student.subjects]
        subjects = (
            db.session.query(Subject)
            .join(RelationStudentSubjectTable)
            .filter(RelationStudentSubjectTable.c.studentId == student.id)
            .filter(Subject.id.in_(subjectIDs))
            .all()
        )

        student = {'Student': getStudent(student)}
        student['Student']['Subjects'] = [
            getSubject(subject) for subject in subjects]
        logging.info(f"{color(2,'Get Student Subjects Complete')} ✅")
    except Exception as e:
        logging.error(
            f"{color(1,'Get Student Subjects Failed')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
        student = None
    return student


def formatDateObjsSubject(subjects: dict[str, str]) -> dict[str, str]:
    '''Formats the date objects in the subject dictionary'''
    subjects['startDate'] = subjects['startDate'].strftime('%Y-%m-%d')
    subjects['endDate'] = subjects['endDate'].strftime('%Y-%m-%d')
    subjects['startTime'] = subjects['startTime'].strftime('%H:%M')
    subjects['endTime'] = subjects['endTime'].strftime('%H:%M')
    subjects['creationDate'] = subjects['creationDate'].strftime(
        '%Y-%m-%d %H:%M:%S')
    subjects['lastupDate'] = subjects['lastupDate'].strftime(
        '%Y-%m-%d %H:%M:%S')
    return subjects


def getScheduleContent(browser: ChromeBrowser) -> list[dict[str, str]]:
    '''Extracts the schedule content from the schedule page and returns a list of dictionaries with the schedule data'''
    try:
        loads = loadScheduleData(
            findScheduleSubjects(findScheduleTable(browser)))
        subjects_data = [getSubject(Subject.query.filter_by(
            group=subject['group'], day=subject['day']).first()) for subject in loads]
    except Exception as e:
        logging.error(
            f"{color(1,'Schedule content not extracted')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
        loads = None
    return subjects_data


def createCompatibleSchedule(subjects: Subject) -> list[Subject]:
    '''Creates a compatible schedule for the student based on the subjects in database'''
    try:
        days = {"Lunes": 0, "Martes": 1, "Miércoles": 2,
                "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
        sorted_subjects = sorted(subjects, key=lambda subject: (
            days[subject.day], subject.startTime))

        schedule = [getSubject(sorted_subjects[i])
                    for i in range(len(sorted_subjects))]

        # create a list of days

    except Exception as e:
        logging.error(
            f"{color(1,'Compatible Schedule Not Created')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
        schedule = None
    return schedule
