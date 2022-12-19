# selenium 4

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os.path
import os
import dotenv

# Setup chrome options
chromeOptions = Options()
chromeOptions.add_argument("--headless")  # Ensure GUI is off
chromeOptions.add_argument("--no-sandbox")

# Set path to chromedriver as per your configuration
homedir = os.path.expanduser("~")
webdriverService = Service(f"{homedir}/chromedriver/stable/chromedriver")

# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriverService, options=chromeOptions)

# Get page UP4U
browser.get("https://up4u.up.edu.mx/user/auth/login")

# Extract inputs for username and password
inputUsername = browser.find_element(
    By.XPATH, "//input[@name='Login[username]']")
inputPassword = browser.find_element(
    By.XPATH, "//input[@name='Login[password]']")
# if both inputs where found print success
print("Username and password fields found ✅") if inputUsername and inputPassword else print(
    "Username and password fields not found ❌")


# define username and password
dotenv.load_dotenv()
username = os.getenv("UP4U_USERNAME", )
password = os.getenv("UP4U_PASSWORD", )
# print username and password
print(f"Username: {username}, Password: {password}")

# Fill inputs with username and password
inputUsername.send_keys(username)
inputPassword.send_keys(password)

# Click on login button
loginButton = browser.find_element(By.XPATH, "//button[@id='login-button']")
loginButton.click()

# copy the page source to horario.html
with open("horario.html", "w") as f:
    f.write(browser.page_source)

# close the browser
browser.close()
