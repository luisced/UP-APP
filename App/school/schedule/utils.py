from school.models import ChromeBrowser, Subject
from school import db
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
import re
import traceback
import logging


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
    subject_data = cleanScheduleData(subjects)
    for data in subject_data:
        data['day'] = data['day'] if data['day'] else current_day
        createSubject(**data)
        current_day = data['day']
    return subject_data


def createSubject(day: str, start_time: datetime, end_time: datetime, subject: str, teacher: str, start_date: datetime, end_date: datetime, group: str, classroom: str):
    '''Creates a subject object'''
    try:

        if not Subject.query.filter_by(group=group, day=day).first():
            subject = Subject(day=day, startTime=start_time, endTime=end_time, name=subject, teacher=teacher,
                              startDate=datetime.strptime(start_date, '%d/%m/%Y'), endDate=datetime.strptime(end_date, '%d/%m/%Y'), group=group, classroom=classroom)
            db.session.add(subject)
            db.session.commit()
        else:
            raise ValueError("Subject already exists in the database")
    except Exception as e:
        logging.error(
            f"\033[31mSubject not created\033[0m ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
        subject = None
    return subject


def getSubject(subject: Subject) -> dict[str, str]:
    '''Returns the subject data as a dictionary'''
    subjects = Subject.to_dict(Subject.query.filter_by(id=subject.id).first())

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


def getScheduleContent(browser: ChromeBrowser) -> list[dict[str, str]]:
    '''Extracts the schedule content from the schedule page and returns a list of dictionaries with the schedule data'''
    try:
        loads = loadScheduleData(
            findScheduleSubjects(findScheduleTable(browser)))
        print("Schedule content extracted ✅")
        try:
            subjects_data = [getSubject(Subject.query.filter_by(
                group=subject['group'], day=subject['day']).first()) for subject in loads]
            print("Schedule content loaded ✅")
        except Exception as e:
            print(
                f"Schedule content not loaded ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
            subjects_data = None
    except Exception as e:
        print(
            f"Schedule content not extracted ❌: {e}\n{traceback.format_exc().splitlines()[-3]}")
        loads = None
    return subjects_data


# def scheduleExcel(subjects: list[Subject]) -> pd:
#     '''Exports the schedule to an excel file'''
#     # Create a new Excel workbook
#     workbook = openpyxl.Workbook()

#     # Get the active worksheet
#     worksheet = workbook.active

#     # Set the column width
#     worksheet.column_dimensions['A'].width = 10
#     for i in range(2, 7):
#         worksheet.column_dimensions[f"{chr(i+64)}"].width = 10

#     # Leave cell A1 blank
#     worksheet.cell(row=1, column=1).value = ""

#     # Write the hours and half-hours in column A, starting at row 2
#     for hour in range(7, 21):
#         worksheet.cell(row=hour*2-11, column=1).value = f"{hour}:00"
#         worksheet.cell(row=hour*2-10, column=1).value = f"{hour}:30"

#     # Write the days of the week in Spanish in columns B to G, starting at row 1
#     days_of_week_spanish = ["Lunes", "Martes", "Miércoles",
#                             "Jueves", "Viernes", ]
#     for i, day in enumerate(days_of_week_spanish):
#         worksheet.cell(row=1, column=i+2).value = day

#     #  Write subject content in the cells
#     # for subject in subjects:
#     #     start_time = subject.startTime
#     #     end_time = subject.endTime
#     #     day = subject.day
#     #     # Get the row and column of the start time
#     #     start_row = (start_time * 2) - 11
#     #     start_column = days_of_week_spanish.index(day) + 2
#     #     # Get the row and column of the end time
#     #     end_row = (end_time * 2) - 10
#     #     end_column = days_of_week_spanish.index(day) + 2
#     #     # Write the subject name in the cells
#     #     for row in range(start_row, end_row+1):
#     #         for column in range(start_column, end_column+1):
#     #             worksheet.cell(row=row, column=column).value = subject.name

#     # Check if the file already exists and delete it if it does
#     if os.path.exists("hours.xlsx"):
#         os.remove("hours.xlsx")

#     # Save the workbook
#     workbook.save("hours.xlsx")

#     print("Hours and days of the week written to Excel file successfully!")
# # df = pd.DataFrame(subjects)
# # df.to_excel('schedule.xlsx', index=False)
