from chrome import ChromeBrowser
from login import login
from menu import findScheduleLink
from schedule import *


if __name__ == "__main__":
    browser = ChromeBrowser().buildBrowser()
    browser.get("https://up4u.up.edu.mx/user/auth/login")
    login = login(browser)
    scheduleLink = findScheduleLink(browser)
    scheduleContent = getScheduleContent(browser)

    print(scheduleContent)

    scheduleExcel(scheduleContent)
    with open("horario.html", "w") as f:
        f.write(browser.page_source)
    browser.quit()
