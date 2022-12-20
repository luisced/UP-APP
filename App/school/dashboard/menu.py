from App.school.tools.chrome import ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def findScheduleLink(browser: ChromeBrowser) -> str:
    '''Extracts the schedule link from the main page'''
    try:
        browser.find_element(By.LINK_TEXT, "Horarios").click()
        time.sleep(3)
        print("Schedule link found ✅\nLoading schedule...")
    except NoSuchElementException:
        print("Schedule link not found ❌")

    return f'Current URL after main menu: \033[94m{browser.current_url}\033[0m'
