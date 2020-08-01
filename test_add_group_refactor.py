from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_add_group():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def open_home_page(self):
    # open home page
    self.driver.get("http://localhost/addressbook/")

  def login(self):
    # login
    self.driver.find_element(By.NAME, "user").click()
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys("secret")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_groups_page(self):
    # open groups page
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def create_group(self):
    # init group creation
    self.driver.find_element(By.NAME, "new").click()
    # fill group form
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys("group")
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys("gh")
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys("gf")
    # submit group creation
    self.driver.find_element(By.NAME, "submit").click()

  def return_to_groups_page(self):
    # return to groups page
    self.driver.find_element(By.LINK_TEXT, "group page").click()

  def logout(self):
    # logout
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def test_add_group(self):
    # все действия выделены в отдельные методы. Метод - это функция внутри класса.
    self.open_home_page()
    self.login()
    self.open_groups_page()
    self.create_group()
    self.return_to_groups_page()
    self.logout()












  
