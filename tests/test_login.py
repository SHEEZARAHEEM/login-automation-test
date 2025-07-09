import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")
        self.driver.maximize_window()

    def test_valid_login(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        self.assertIn("Logged In Successfully", driver.page_source)

    def test_invalid_password(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "password").send_keys("wrongpass")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        self.assertIn("Your password is invalid!", driver.page_source)

    def test_invalid_username(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        self.assertIn("Your username is invalid!", driver.page_source)

    def test_empty_username(self):
        driver = self.driver
        driver.find_element(By.ID, "password").send_keys("Password123")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        self.assertIn("Your username is invalid!", driver.page_source)

    def test_empty_password(self):
        driver = self.driver
        driver.find_element(By.ID, "username").send_keys("student")
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        self.assertIn("Your password is invalid!", driver.page_source)

    def test_empty_fields(self):
        driver = self.driver
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        self.assertIn("Your username is invalid!", driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
