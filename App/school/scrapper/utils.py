from school.models import ChromeBrowser
from school.dashboard.utils import findScheduleLink
from school.schedule.utils import *
from school.login.utils import login


def extractUP4USchedule() -> list[Subject]:
    browser = ChromeBrowser().buildBrowser()
    browser.get("https://up4u.up.edu.mx/user/auth/login")
    login(browser)
    # scheduleLink = findScheduleLink(browser)
    # scheduleContent = getScheduleContent(browser)

    def get_schedule(browser): return getScheduleContent(
        findScheduleLink(browser))

    return get_schedule
