from chrome import ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dataclasses import dataclass
from datetime import datetime
import re


@dataclass
class Subject:
    '''Class to represent a subject'''
    name: str
    teacher: str
    classroom: str
    day: str
    startTime: datetime
    endTime: datetime
    startdate: datetime
    enddate: datetime
    group: str

    def __str__(self) -> str:
        return f'Subject:{" - ".join([f"{column.name}:{getattr(self, column.name)}" for column in self.__table__.columns])})'

    def to_dict(self) -> dict:
        '''Convert the subject to a dictionary'''
        return self.__dict__

    def __format__(self, format_spec) -> str:
        '''Format the subject as a table'''
        # Create a list of tuples, where each tuple contains the name and value of an attribute
        data = [(column.name, getattr(self, column.name))
                for column in self.__table__.columns]

        # Find the maximum length of the attribute names, so we can align the values properly
        max_name_length = max(len(name) for name, value in data)

        # Create a list of strings that represents each row in the table
        rows = []
        for name, value in data:
            # Left-align the attribute name and right-align the value
            row = '{:{}}: {}'.format(name, max_name_length, value)
            rows.append(row)

        # Join the rows with newline characters to create the final table string
        return '\n'.join(rows)


def findScheduleTable(browser):
    try:
        scheduleContent = browser.find_element(By.ID, "contenido-tabla")
        print("Schedule content found ✅")
    except NoSuchElementException:
        print("Schedule content not found ❌")
    return scheduleContent


def findScheduleSubjects(scheduleContent: str) -> list[str]:
    '''Extracts the schedule subjects from the schedule content'''
    try:
        rows = scheduleContent.find_elements(By.CSS_SELECTOR, "div.row")
        print(f"Schedule content has {len(rows)} rows🔎")
    except NoSuchElementException:
        print("Schedule content has no rows ❌")

    data = []
    for row in rows:
        # Find all the div elements within the row
        cells = row.find_elements(By.CSS_SELECTOR, 'div')

        # Extract the data from the cells
        cell_data = [cell.text for cell in cells]

        # Add the data to the list
        data.append(cell_data)

    return data


def splitScheduleSubjects(scheduleRows: list[list[str]]) -> list[Subject]:
    '''Splits the schedule subjects into a list of subjects'''
    cell = [row for row in scheduleRows]
    # Extract the data from the row
    objects: list[Subject] = []
    for data in cell:
        day = data[1]
        start_time = data[2]
        end_time = data[3]
        subject = data[4]
        teacher = data[6]
        start_date = data[7]
        end_date = data[8]
        group = data[9]
        classroom = data[5]

        # Use regex to remove the newline characters from the data
        day = re.sub(r'\n', '', day)
        start_time = re.sub(r'\n', '', start_time)
        end_time = re.sub(r'\n', '', end_time)
        subject = re.sub(r'\n', '', subject)
        teacher = re.sub(r'\n', '', teacher)
        start_date = re.sub(r'\n', '', start_date)
        end_date = re.sub(r'\n', '', end_date)
        group = re.sub(r'\n', '', group)
        classroom = re.compile(
            r'([^/]*)$').search(re.sub(r'\n', '', classroom)).group(1).replace('Ver', '').lstrip()

        # Create a Subject object
        objects.append(createSubject(day, start_time, end_time, subject,
                                     teacher, start_date, end_date, group, classroom))

    # convert list of objects to list of dictionaries
    # objects = [subject.to_dict() for subject in objects]

    return objects


def createSubject(day: str, start_time: datetime, end_time: datetime, subject: str, teacher: str, start_date: datetime, end_date: datetime, group: str, classroom: str):
    '''Creates a subject object'''

    subject = Subject(day=day, startTime=start_time, endTime=end_time, name=subject, teacher=teacher,
                      startdate=start_date, enddate=end_date, group=group, classroom=classroom)

    return subject


def getScheduleContent(browser: ChromeBrowser) -> list[list[str]]:
    '''Extracts the schedule content from the schedule page'''
    scheduleContent = findScheduleTable(browser)

    scheduleSubjects = findScheduleSubjects(scheduleContent)

    splited_subject = splitScheduleSubjects(scheduleSubjects)

    return splited_subject
