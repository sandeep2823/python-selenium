from selenium import webdriver
from Pages.loginPage import LoginPage
from Pages.HomePage import HomePage
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))



class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/sandeepsingh/Study/projects/Python/projects/H3U/drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://www.h3u.com/itgi/#!/login/")

        login = LoginPage(driver)
        login.enter_username("12345")
        time.sleep(1)
        login.enter_password("1234567")
        time.sleep(1)
        login.click_login_button()

        homepage = HomePage(driver)
        time.sleep(1)
        homepage.click_on_logout()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/sandeepsingh/Study/projects/Python/projects/H3U/Reports'))
