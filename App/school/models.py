from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os.path


@dataclass
class ChromeBrowser:
    """Class to create a Chrome browser instance"""

    def buildBrowser(self) -> webdriver:
        """Method to build a Chrome browser instance"""
        """Constructor method to initialize the Chrome browser instance"""
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--headless")  # Ensure GUI is off
        chromeOptions.add_argument("--no-sandbox")

        browser = webdriver.Remote(
            command_executor='http://localhost:3000',
            options=chromeOptions
        )
        return browser
