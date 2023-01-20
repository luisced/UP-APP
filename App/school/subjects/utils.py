from school import db
from school.models import Subject, ChromeBrowser
from school.tools.utils import color
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import re
import logging
import traceback


def createSubject(name: str):
    '''Creates a subject object'''
    try:

        if not Subject.query.filter_by(name=subject).first():
            subject = Subject(name=name)
            # Subject(day=day, startTime=start_time, endTime=end_time, name=subject, teacher=teacher,
            #                   startDate=datetime.strptime(start_date, '%d/%m/%Y'), endDate=datetime.strptime(end_date, '%d/%m/%Y'), group=group, )

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


def extractSubjectsFromTable(browser: ChromeBrowser) -> list[str]:
    '''Once the html table was located, it scrappes the subjects out
       of it and returns a list of list, each list represents a subject '''
    try:
        rows = browser.find_elements(
            By.XPATH, '//*[@id="ACE_$ICField$4$$0"]/tbody/tr')

        logging.info(
            f"{color(2,'Subjects content found')} ✅")
    except NoSuchElementException:
        logging.error(
            f"{color(1,'Subjects content not found')} ❌")

    return rows


def splitListCourses(rows: list[str]) -> list[list[str]]:
    '''Given a list of courses, it splits them into a list of lists, each list represents a course'''
    # The try-except block is used to catch any errors that may occur and log them
    try:
        # The map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)
        # In this case, the given function is the lambda function, which splits the text of each row using the new line character (\n) as a separator
        # The result of this is a list of lists, each sublist contains the text of each row
        subjectData = list(map(lambda x: [line for line in x[0].splitlines()], [
                           [row.text.strip()] for row in rows]))

        separated_classes = []
        current_group = []
        # The for loop iterates over each list in the subjectData list and stores the result of each iteration in the sub_list variable
        for sub_list in subjectData:
            # The for loop iterates over each element in the sub_list variable and stores the result of each iteration in the item variable
            for item in sub_list:
                # The if statement verifies that the item variable is not equal to the string "Clase Sección Días y Horas Aula Instructor Idioma Inscr / Cap Estado      "
                if item != "Clase Sección Días y Horas Aula Instructor Idioma Inscr / Cap Estado      ":
                    # If the condition is true, the item variable is appended to the current_group list
                    current_group.append(item)
                else:
                    # If the condition is false, the if statement verifies that the current_group list is not empty
                    if current_group:
                        # If the condition is true, the current_group list is appended to the separated_classes list
                        separated_classes.append(current_group)
                    # The current_group list is reset to a list containing the first element of the sub_list variable
                    current_group = [sub_list[0]]
            # The if statement verifies that the current_group list is not empty
            if current_group:
                # If the condition is true, the current_group list is appended to the separated_classes list
                separated_classes.append(current_group)
            # The current_group list is reset to an empty list
            current_group = []
        logging.info(
            f"{color(2,'Courses split successfully')} ✅")
    # If an error occurs, the except block is executed
    except Exception as e:
        logging.error(
            f"{color(1,'Courses not split')} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
    # The function returns a list containing only the courses in separated_classes that have more than one element
    return [course for course in separated_classes if len(course) > 1]


def fetchSubjectData(browser: ChromeBrowser) -> str:
    '''Fetches the subject data from the html'''
    subjectData: list[list[str]] = (
        splitListCourses(extractSubjectsFromTable(browser)))
    # print(cleanSubjectText())

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
