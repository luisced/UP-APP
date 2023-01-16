from school import db
from school.models import Subject, ChromeBrowser
from school.tools.utils import color
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import logging
import traceback


def createSubject(day: str, start_time: datetime, end_time: datetime, subject: str, teacher: str, start_date: datetime, end_date: datetime, group: str):
    '''Creates a subject object'''
    try:

        if not Subject.query.filter_by(name=subject).first():
            subject = Subject(day=day, startTime=start_time, endTime=end_time, name=subject, teacher=teacher,
                              startDate=datetime.strptime(start_date, '%d/%m/%Y'), endDate=datetime.strptime(end_date, '%d/%m/%Y'), group=group, )

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


def extractSubjectsFromTable(browser: str) -> list[str]:
    '''Once the html table was located, it scrappes the subjects out of it'''
    try:
        rows = browser.find_elements(
            By.XPATH, '//*[@id="ACE_$ICField$4$$0"]/tbody')
        logging.info(
            f"{color(2,'Subjects content found')} ✅")
    except NoSuchElementException:
        logging.error(
            f"{color(1,'Subjects content not found')} ❌")

    return [row.text for row in rows]


# def cleanSubjectText(subjectText: str) -> list[str]:
#     '''Cleans the subject text from the html table sent from extractSubjectsFromTable function'''
#     try:


#     return None
# Remove the first 2 elements


def fetchSubjectData(browser: ChromeBrowser) -> str:
    '''Fetches the subject data from the html'''
    cleanSubjectText(extractSubjectsFromTable(browser))

    # create html file swith source code

    # try:s

    #     # Get the table
    #     table = source_html.find('table', {'class': 'PSLEVEL3GRID'})
    #     # Get the rows
    #     rows = table.find_all('tr', {'class': 'PSLEVEL3'
    #                                     'GRIDROW'})
    #     # Get the columns
    #     columns = [row.find_all('td') for row in rows]
    #     # Get the data
    #     data = [[column.text for column in row] for row in columns]
    #     # Get the subjects
    #     subjects = [getSubjectData(row) for row in data]
    #     # Create the subjects
    #     [createSubject(**subject) for subject in subjects]
    #     return 'Subjects created'
    # except Exception as e:
    #     logging.critical(
    #         f'{color(5,"Schedule extraction failed")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
    #     return 'Subjects not created'
