# selenium 4

from chrome import ChromeBrowser
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os.path
import os
import dotenv
import time


browser = ChromeBrowser().buildBrowser()

# Get page UP4U
browser.get("https://up4u.up.edu.mx/user/auth/login")


# Extract inputs for username and password and id
try:
    inputUsername = browser.find_element(
        By.XPATH, "//input[@name='Login[username]' and @id='login_username']")
except NoSuchElementException:
    print("Username field not found ❌")
try:
    inputPassword = browser.find_element(
        By.XPATH, "//input[@name='Login[password]'and @id='login_password'] ")
except NoSuchElementException:
    print("Password field not found ❌")


# define username and password
dotenv.load_dotenv()
username = os.getenv("UP4U_USERNAME", )
password = os.getenv("UP4U_PASSWORD", )

# Fill inputs with username and password
inputUsername.send_keys(username)
inputPassword.send_keys(password)
# inputPassword.send_keys(Keys.RETURN)

# Click on login button
try:
    loginButton = browser.find_element(By.ID, "login-button")
except NoSuchElementException:
    print("Login button not found ❌")
loginButton.click()

if "User or Password incorrect." in browser.page_source or "contraseña no puede estar vacío." in browser.page_source:
    print("Error message found, login failed ❌")
else:
    print("Login successful ✅")

# Wait for the page to load
print("Waiting for the page to load... 🕒\nLet me sleep for 3 seconds\nZZzzzz...")
time.sleep(3)
print("Page loaded ✅")
print(browser.current_url)

# copy the page source to horario.html
with open("horario.html", "w") as f:
    f.write(browser.page_source)
