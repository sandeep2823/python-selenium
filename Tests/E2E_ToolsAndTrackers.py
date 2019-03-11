from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.ToolsAndTrackersPage import ToolsAndTrackersPage
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class E2EToolsAndTrackersTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path="/Users/sandeepsingh/Study/projects/Python/projects/H3U/drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        driver = cls.driver
        driver.get("https://www.h3u.com/itgi/#!/login/")
        login = LoginPage(cls.driver)
        login.enter_username("12345")
        login.enter_password("1234567")
        login.click_login_button()
        homepage = HomePage(cls.driver)
        time.sleep(1)
        homepage.click_on_tools_and_trackers()
        time.sleep(1)

    def test_tools_and_trackers_bmi_meter(self):
        toolsntracker = ToolsAndTrackersPage(self.driver)
        toolsntracker.validate_bmi_meter_text("BMI Meter")
        toolsntracker.click_on_bmi_meter()
        time.sleep(1)
        toolsntracker.click_on_back_button()
        time.sleep(1)

    def test_tools_and_trackers_salt_meter(self):
        toolsntracker = ToolsAndTrackersPage(self.driver)
        toolsntracker.validate_salt_meter_text("Salt Meter")
        toolsntracker.click_on_salt_meter()
        time.sleep(1)
        toolsntracker.click_on_back_button()
        time.sleep(1)

    def test_tools_and_trackers_smoke_meter(self):
        toolsntracker = ToolsAndTrackersPage(self.driver)
        toolsntracker.validate_smoke_meter_text("Smoke Meter")
        toolsntracker.click_on_smoke_meter()
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/sandeepsingh/Study/projects/Python/projects/H3U/Reports'))
