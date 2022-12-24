from school.models import ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from school.tools.utils import color
import time
import logging


def findScheduleLink(browser: ChromeBrowser) -> str:
    '''Extracts the schedule link from the main page'''
    try:
        browser.find_element(By.LINK_TEXT, "Horarios").click()
        time.sleep(3)
        logging.info(f'{color(2,"Loading schedule...")} ✅')
    except NoSuchElementException:
        logging.error(f'{color(1,"Schedule link not found")} ❌')

    return f'Current URL after main menu: \033[94m{browser.current_url}\033[0m'
