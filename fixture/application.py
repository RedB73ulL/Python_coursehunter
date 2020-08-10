from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper

class Application():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
