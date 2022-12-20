from school.models import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import dotenv
import time


def findUsernameInput(browser: ChromeBrowser) -> str:
    '''Extracts the username input from the login page'''
    try:
        inputUsername = browser.find_element(
            By.XPATH, "//input[@name='Login[username]' and @id='login_username']")
    except NoSuchElementException:
        print("Username field not found ❌")
    return inputUsername


def findPasswordInput(browser: ChromeBrowser) -> str:
    '''Extracts the password input from the login page'''
    try:
        inputPassword = browser.find_element(
            By.XPATH, "//input[@name='Login[password]'and @id='login_password'] ")
    except NoSuchElementException:
        print("Password field not found ❌")
    return inputPassword


# define username and password
def fillUsernameInput(inputUsername) -> str:
    '''Fills the username input with the username'''
    dotenv.load_dotenv()
    username = os.getenv("UP4U_USERNAME", )
    inputUsername.send_keys(username)
    input_value = inputUsername.get_attribute("value")
    return input_value


# Fill inputs with username and password
def fillPassswordInput(inputPassword) -> str:
    '''Fills the password input with the password'''
    dotenv.load_dotenv()
    password = os.getenv("UP4U_PASSWORD", )
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
        print("Login button not found ❌")


def login(browser: ChromeBrowser) -> str:
    '''Logs in to the UP4U page'''
    try:
        username = fillUsernameInput(findUsernameInput(browser))
        password = fillPassswordInput(findPasswordInput(browser))
        print(f'Username: {username}\nPassword: {password}')
        clickLoginButton(browser)
        if browser.find_element(By.CLASS_NAME, "help-block").text == "User or Password incorrect.":
            print("Error message found, login failed ❌")
        else:
            print(
                f"Login successful ✅\nWaiting for the page to load... 🕒\nLet me sleep for 3 seconds\nZZzzzz...")
            time.sleep(3)
            print("Main Menu loaded ✅")
    except Exception as e:
        print(f'Login failed ❌\n{e}')
    # color the url blue in the terminal
    return f'Current URL after login: \033[94m{browser.current_url}\033[0m'
