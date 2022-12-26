from school.student.utils import createStudent
from school.models import ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from school.tools.utils import color
from flask import session
import time
import logging
import traceback


def enterDashboard(browser: ChromeBrowser) -> str:
    '''Extracts the schedule link from the main page'''
    try:
        try:
            userName = browser.find_element(
                By.XPATH, "//div[@class='user-title pull-left hidden-xs']").find_element(By.XPATH, "//strong").text
            createStudent(**session['student'], name=userName)
        except NoSuchElementException:
            logging.error(
                f'{color(1,"Couldnt create student")} ❌ {traceback.format_exc().splitlines()[-3]}')

        browser.find_element(By.LINK_TEXT, "Horarios").click()
        time.sleep(3)
        logging.info(f'{color(2,"Loading schedule...")} ✅')
    except NoSuchElementException:
        logging.error(f'{color(1,"Schedule link not found")} ❌')

    return f'Current URL after main menu: \033[94m{browser.current_url}\033[0m'
