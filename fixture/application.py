from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from fixture.group_helper import GroupHelper
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.wd.implicitly_wait(30)
        self.group = GroupHelper(self)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()




