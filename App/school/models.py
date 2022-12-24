from school import db
from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import os.path


@dataclass
class ChromeBrowser:
    """Class to create a Chrome browser instance"""

    def __init__(self):
        """Constructor method to initialize the Chrome browser instance"""
        self.chromeOptions = Options()
        self.chromeOptions.add_argument("--headless")  # Ensure GUI is off
        self.chromeOptions.add_argument("--no-sandbox")
        self.chromeOptions.add_argument("--disable-dev-shm-usage")

    def buildBrowser(self) -> webdriver:
        """Method to build a Chrome browser instance"""
        webdriverService = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(
            service=webdriverService, options=self.chromeOptions)
        return browser


@dataclass
class Subject(db.Model):
    '''Model to represent a subject for storing subjects in the database'''

    __tablename__ = 'Subject'

    id: int = db.Column(db.Integer, primary_key=True,
                        autoincrement=True, nullable=False)
    name: str = db.Column(db.String(280), nullable=False)
    teacher: str = db.Column(db.String(280), nullable=False)
    classroom: str = db.Column(db.String(280), nullable=False)
    day: str = db.Column(db.String(280), nullable=False)
    startTime: str = db.Column(db.Time, nullable=False)
    group: str = db.Column(db.String(280), nullable=False)
    endTime: str = db.Column(db.Time, nullable=False)
    startdate: datetime = db.Column(db.Date, nullable=False)
    enddate: datetime = db.Column(db.Date, nullable=False)
    status: bool = db.Column(db.Boolean, nullable=False, default=True)
    creationdate: datetime = db.Column(
        db.Date, nullable=False, default=datetime.now)
    lastupdate: str = db.Column(
        db.TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now)
    option = db.Column(db.Integer, nullable=False, default=0)

    def __repr__(self) -> str:
        '''Convert the subject to a string'''
        return f'Subject:{" ".join([f"{column.name}={getattr(self, column.name)}" for column in self.__table__.columns])}'

    def to_dict(self) -> dict:
        '''Convert the subject to a dictionary'''
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
