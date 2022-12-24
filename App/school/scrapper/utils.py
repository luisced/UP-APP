from school.models import ChromeBrowser
from school.dashboard.utils import findScheduleLink
from school.schedule.utils import *
from school.login.utils import *
from school.tools.utils import color
import traceback
import logging


def extractUP4USchedule(studentId: str, password: str) -> list[Subject]:
    '''Extracts the schedule of a student from the UP4U platform'''
    try:
        browser = ChromeBrowser().buildBrowser()
        browser.get("https://up4u.up.edu.mx/user/auth/login")
        login(browser, studentId, password)
        findScheduleLink(browser)
        scheduleContent = getScheduleContent(browser)
    except Exception as e:
        logging.error(
            f'{color(1,"Schedule extraction failed")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
        scheduleContent = None

    return scheduleContent
