from selenium import webdriver
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.CustomerDetailsPage import CustomerDetailsPage
import time
import unittest
import HtmlTestRunner
import sys
import os
from selenium.webdriver.chrome.options import Options
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class E2EHealthCardTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")

        chrome_options.add_argument("window-size=1800x1080")

        chrome_options.add_argument("--disable-dev-shm-usage")
        cls.driver = webdriver.Chrome(
            executable_path="/usr/bin/chromedriver",
        chrome_options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_customer_name_displays(self):
        driver = self.driver
        driver.get("https://www.h3u.com/itgi/#!/login/")

        login = LoginPage(driver)
        login.enter_username("12345")
        login.enter_password("1234567")
        login.click_login_button()

        homepage = HomePage(driver)
        homepage.click_on_heath_card()

        customerpage = CustomerDetailsPage(driver)
        customerpage.validate_customer_name("SUDHIR  MITTAL")

        customerpage.click_customer_name()
        time.sleep(4)
        customerpage.validate_health_card_detail_dialogue_box("Health Card Details")
        print("Health card detail is displayed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/sandeepsingh/Study/projects/Python/projects/H3U/Reports'))
