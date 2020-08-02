from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group

class Test_add_group():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def open_home_page(self):
    # open home page
    self.driver.get("http://localhost/addressbook/")

  def login(self, username, password):
    # login
    self.open_home_page()
    self.driver.find_element(By.NAME, "user").click()
    self.driver.find_element(By.NAME, "user").send_keys(username)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_groups_page(self):
    # open groups page
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def create_group(self, group):
    # init group creation
    self.open_groups_page()
    self.driver.find_element(By.NAME, "new").click()
    # fill group form
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
    # submit group creation
    self.driver.find_element(By.NAME, "submit").click()
    self.return_to_groups_page()

  def return_to_groups_page(self):
    self.driver.find_element(By.LINK_TEXT, "group page").click()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def test_add_group(self):
    self.login(username="admin", password="secret")
    self.create_group(Group(name="group", header="gh", footer="gf"))
    self.logout()

  def test_add_empty_group(self):
    self.login(username="admin", password="secret")
    self.create_group(Group(name="", header="", footer=""))
    self.logout()
