from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        # init group creation
        self.open_groups_page()
        self.app.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.app.driver.find_element(By.NAME, "group_name").click()
        self.app.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.app.driver.find_element(By.NAME, "group_header").click()
        self.app.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.app.driver.find_element(By.NAME, "group_footer").click()
        self.app.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.app.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.app.driver.find_element(By.LINK_TEXT, "group page").click()

    def delete_first_group(self):
        # init group creation
        self.open_groups_page()
        # select first group
        self.app.driver.find_element(By.NAME, "selected[]").click()
        # submit deletion
        self.app.driver.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()