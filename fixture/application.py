from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application():
    def __init__(self, browser, base_url):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError("Unrecognize browser %s" % browser)
        self.driver.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        self.driver.get(self.base_url)

    def destroy(self):
        self.driver.quit()

    def is_valid(self):
        try:
            self.driver.current_url
            return True
        except:
            return False
