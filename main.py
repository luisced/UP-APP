from chrome import ChromeBrowser
from login import login
from menu import findScheduleLink
from schedule import getScheduleContent, formatSubject


if __name__ == "__main__":
    browser = ChromeBrowser().buildBrowser()
    browser.get("https://up4u.up.edu.mx/user/auth/login")
    login = login(browser)
    scheduleLink = findScheduleLink(browser)
    scheduleContent = getScheduleContent(browser)

# list to dict
    print([s.__dict__ for s in scheduleContent])
    with open("horario.html", "w") as f:
        f.write(browser.page_source)
    browser.quit()
