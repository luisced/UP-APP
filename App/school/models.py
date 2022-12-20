from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os.path


@dataclass
class ChromeBrowser:
    """Class to create a Chrome browser instance"""

    def __init__(self):
        """Constructor method to initialize the Chrome browser instance"""
        self.chromeOptions = Options()
        self.chromeOptions.add_argument("--headless")  # Ensure GUI is off
        self.chromeOptions.add_argument("--no-sandbox")

    def buildBrowser(self) -> webdriver:
        """Method to build a Chrome browser instance"""
        homedir = os.path.expanduser("~")
        webdriverService = Service(
            f"{homedir}/chromedriver/stable/chromedriver")
        browser = webdriver.Chrome(
            service=webdriverService, options=self.chromeOptions)
        return browser
