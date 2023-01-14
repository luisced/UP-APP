from school.models import ChromeBrowser
from school.dashboard.utils import enterDashboard, enterDashboardUPSite
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
        enterDashboard(browser)
        scheduleContent = getScheduleContent(browser)
    except Exception as e:
        logging.critical(
            f'{color(5,"Schedule extraction failed")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
        scheduleContent = None

    return scheduleContent


def extractUPSiteSchedule(studentId: str, password: str) -> list[Subject]:
    '''Extracts the schedule of a student from the UP site'''
    try:
        # Start the browser
        with ChromeBrowser().buildBrowser() as browser:
            # Go to the main page
            browser.get(
                "https://upsite.up.edu.mx/psp/CAMPUS/?cmd=login&languageCd=ESP&")
            # Login
            loginUPSite(browser, studentId, password)
            # Enter the dashboard
            enterDashboardUPSite(browser)

            # Get the schedule content
            subjectData = fetchSubjectData(browser)

    except Exception as e:
        logging.critical(
            f'{color(5,"Schedule extraction failed")} ❌: {e}\n{traceback.format_exc().splitlines()[-3]}')
