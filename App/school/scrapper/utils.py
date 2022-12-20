from App.school.tools.chrome import ChromeBrowser
from App.school.login.utils import login
from App.school.dashboard.menu import findScheduleLink
from App.school.schedule.utils import *


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
