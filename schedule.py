from chrome import ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dataclasses import dataclass
from datetime import datetime


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
    modality: str

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


def getScheduleContent(browser: ChromeBrowser) -> list[list[str]]:
    '''Extracts the schedule content from the schedule page'''
    scheduleContent = findScheduleTable(browser)

    scheduleSubjects = findScheduleSubjects(scheduleContent)

    return scheduleSubjects


def findScheduleSubjects(scheduleContent: str) -> list[str]:
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


def findScheduleTable(browser):
    try:
        scheduleContent = browser.find_element(By.ID, "contenido-tabla")
        print("Schedule content found ✅")
    except NoSuchElementException:
        print("Schedule content not found ❌")
    return scheduleContent
