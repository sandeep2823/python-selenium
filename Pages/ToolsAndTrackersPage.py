class ToolsAndTrackersPage:
    def __init__(self, driver):
        self.driver = driver

        self.bmi_meter_text = "/html/body/div/div[3]/div/div/div/div[2]/a/div/div/h4/b"
        self.salt_meter_text = "/html/body/div/div[3]/div/div/div/div[3]/a/div/div/h4/b"
        self.smoke_meter_text = "/html/body/div/div[3]/div/div/div/div[4]/a/div/div/h4/b"
        self.back_button = "//a[@id='backButton']/button"

    def validate_bmi_meter_text(self, name):
        bmi_meter_text = self.driver.find_element_by_xpath(self.bmi_meter_text).text
        print(bmi_meter_text)
        assert bmi_meter_text in name

    def validate_salt_meter_text(self, name):
        salt_meter_text = self.driver.find_element_by_xpath(self.salt_meter_text).text
        print(salt_meter_text)
        assert salt_meter_text in name

    def validate_smoke_meter_text(self, name):
        smoke_meter_text = self.driver.find_element_by_xpath(self.smoke_meter_text).text
        print(smoke_meter_text)
        assert smoke_meter_text in name

    def click_on_bmi_meter(self):
        self.driver.find_element_by_xpath(self.bmi_meter_text).click()

    def click_on_salt_meter(self):
        self.driver.find_element_by_xpath(self.salt_meter_text).click()

    def click_on_smoke_meter(self):
        self.driver.find_element_by_xpath(self.smoke_meter_text).click()

    def click_on_back_button(self):
        self.driver.find_element_by_xpath(self.back_button).click()
