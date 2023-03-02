from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from school import db
from school.tools.utils import color
from school.models import Group, Student, Schedule, Classroom, Days, Hours
from school.classrooms.utils import createClassroom, createClassroomSubjectRelationship
from school.days.utils import *
from school.hours.utils import *
from datetime import datetime
import traceback
import logging


def createSchedule(daysHours: list[str], classrooms: list[Classroom], group: Group) -> Schedule:
    '''Creates a schedule taking the days and hours from the schedule content and the classroom and groups objects'''
    try:

        schedule = Schedule(
            dayID=1,  # Dia: str
            startTime='14:00:00',  # Hora de inicio: datetime
            endTime='14:00:00',  # Hora de Fin: datetime
            classroomID=1,  # Salón: id -> int
        )
        db.session.add(schedule)
        db.session.commit()
        print(schedule)
        logging.info(f'{color(2,"Schedule created")} ✅')
    except Exception as e:
        logging.critical(
            f'{color(5,"Schedule creation failed")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
        schedule = None

    return schedule


# def findScheduleTable(browser):
#     try:
#         scheduleContent = browser.find_element(By.ID, "contenido-tabla")
#         logging.info(f'{color(2,"Schedule content found")} ✅')
#     except NoSuchElementException:
#         logging.error(f'{color(1,"Schedule content not found")} ❌')
#     return scheduleContent


# def findScheduleSubjects(scheduleContent: str) -> list[str]:
#     '''Extracts the schedule subjects from the schedule content'''
#     try:
#         rows = scheduleContent.find_elements(By.CSS_SELECTOR, "div.row")
#         logging.info(f'{color(4,f"Schedule content has {len(rows)} rows")}🔎')
#     except NoSuchElementException:
#         logging.warning(f'{color(1,"Schedule content has no rows")} ❌')

#     return [[cell.text for cell in row.find_elements(
#         By.CSS_SELECTOR, 'div')] for row in rows]


# def cleanScheduleData(subjectsList: list[list[Subject]]) -> list[dict[str, str]]:
#     '''Cleans the schedule data'''

#     return [
#         {
#             'day': subjectData[1].strip(),
#             'start_time': subjectData[2].strip(),
#             'end_time': subjectData[3].strip(),
#             'subject': subjectData[4].strip(),
#             'teacher': subjectData[6].strip(),
#             'start_date': subjectData[7].strip(),
#             'end_date': subjectData[8].strip(),
#             'group': subjectData[9].strip(),
#             'classroom': re.compile(r'([^/]*)$').search(re.sub(r'\n', '', subjectData[5].strip())).group(1).replace('Ver', '').lstrip()
#         }
#         for subjectData in subjectsList
#     ]


# def loadScheduleData(scheduleSubjects: list[dict[str, str]]) -> None:
#     '''Loads the schedule data into a Subject object'''
#     current_day = ''
#     subjects = [subject for subject in scheduleSubjects if subject != []]
#     try:
#         subject_data = cleanScheduleData(subjects)
#         for data in subject_data:
#             data['day'] = data['day'] if data['day'] else current_day
#             createSchedule(**data)
#             current_day = data['day']
#         logging.info(f'{color(4,"Schedule data loaded into DB")} ✅')
#     except Exception as e:
#         logging.error(
#             f'{color(1,"Schedule data not loaded into DB")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')


# def createSchedule(day: str, start_time: datetime, end_time: datetime, subject: str, teacher: str, start_date: datetime, end_date: datetime, group: str, classroom: str) -> None:
#     '''Creates a schedule object'''

#     # create objects
#     subject = createSubject(day, start_time, end_time, subject, teacher,
#                             start_date, end_date, group)
#     classroom = createClassroom(classroom)
#     # create relations

#     # createStudentSubjectRelationship(Student.query.filter_by(
#     #     studentID=session['student']['studentID']).first(), subject)


# def getStudentSubjects(student: Student) -> dict:
#     '''Returns the student subjects as a dictionary with his subjects'''
# #     try:

# #         subjects = (
# #             db.session.query(Subject)
# #             .filter(Subject.id.in_((
# #                 db.session.query(RelationStudentSubjectTable.c.subjectId)
# #                 .filter(RelationStudentSubjectTable.c.studentId == student.id)
# #                 .subquery()
# #             )
# #             ))
# #             .all()
# #         )
# #         student = {'Student': getStudent(student)}
# #         student['Student']['Subjects'] = list(map(
# #             lambda subject: getSubject(subject), subjects))
# #         logging.info(f"{color(2,'Get Student Subjects Complete')} ✅")
# #     except Exception as e:
# #         logging.error(
# #             f"{color(1,'Get Student Subjects Failed')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
# #         student = None
# #     return student


# def fetchScheduleContent(browser: ChromeBrowser) -> None:
#     '''Extracts the schedule content from the schedule page and returns a list of dictionaries with the schedule data'''
#     try:
#         loadScheduleData(
#             findScheduleSubjects(findScheduleTable(browser)))
#     except Exception as e:
#         logging.error(
#             f"{color(1,'Schedule content not extracted')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")


# def createCompatibleSchedule(subjects: Subject) -> list[Subject]:
#     '''Creates a compatible schedule for the student based on the subjects in database'''
#     try:
#         days = {"Lunes": 0, "Martes": 1, "Miércoles": 2,
#                 "Jueves": 3, "Viernes": 4, "Sábado": 5, "Domingo": 6}
#         sorted_subjects = sorted(subjects, key=lambda subject: (
#             days[subject.day], subject.startTime))

#         schedule = [getSubject(sorted_subjects[i])
#                     for i in range(len(sorted_subjects))]

#         # create a list of days

#     except Exception as e:
#         logging.error(
#             f"{color(1,'Compatible Schedule Not Created')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
#         schedule = None
#     return schedule
