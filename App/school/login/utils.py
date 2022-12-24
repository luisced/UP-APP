from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from school.models import *
from school.tools.utils import color
import time
import logging


def findUsernameInput(browser: ChromeBrowser) -> str:
    '''Extracts the username input from the login page'''
    try:
        inputUsername = browser.find_element(
            By.XPATH, "//input[@name='Login[username]' and @id='login_username']")
    except NoSuchElementException:
        logging.error(f'{color(1,"Username field not found")} ❌')

    return inputUsername


def findPasswordInput(browser: ChromeBrowser) -> str:
    '''Extracts the password input from the login page'''
    try:
        inputPassword = browser.find_element(
            By.XPATH, "//input[@name='Login[password]'and @id='login_password'] ")
    except NoSuchElementException:
        logging.error(f'{color(1,"Password field not found")} ❌')
    return inputPassword


# define username and password
def fillUsernameInput(inputUsername: str, studentId: str) -> str:
    '''Fills the username input with the username'''
    inputUsername.send_keys(studentId)
    input_value = inputUsername.get_attribute("value")
    return input_value


# Fill inputs with username and password
def fillPassswordInput(inputPassword: str, password: str) -> str:
    '''Fills the password input with the password'''
    inputPassword.send_keys(password)
    input_value = inputPassword.get_attribute("value")
    return input_value

# Click on login button


def clickLoginButton(browser: ChromeBrowser) -> None:
    '''Clicks on the login button'''
    try:
        loginButton = browser.find_element(By.ID, "login-button")
        loginButton.click()
    except NoSuchElementException:
        logging.error(f'{color(1,"Login button not found")} ❌')


def login(browser: ChromeBrowser, studentId: str, password: str) -> str:
    '''Logs in to the UP4U page'''
    try:
        username = fillUsernameInput(findUsernameInput(browser), studentId)
        password = fillPassswordInput(findPasswordInput(browser), password)
        print(f'Username: {username}\nPassword: {password}')
        logging.info(f'Username: {username}\nPassword: {password}')
        clickLoginButton(browser)
        if browser.find_element(By.CLASS_NAME, "help-block").text:
            logging.error(f"{color(1,'Error message found, login failed')} ❌")
        else:
            logging.info(
                f"Login successful ✅\nWaiting for the page to load... 🕒\nLet me sleep for 3 seconds\nZZzzzz...")
            time.sleep(3)
            logging.info("I'm awake now 🤓\nMain Menu loaded ✅")
    except Exception as e:
        print(f'Login failed ❌\n{e}')
        logging.critical(f"{color(5,'Login failed')} ❌\n{e}")
    # color the url blue in the terminal
    return f'Current URL after login: \033[94m{browser.current_url}\033[0m'
