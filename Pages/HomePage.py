class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.logout_link_text = "Logout"
        self.health_card_xpath = "//div[@name='mainContent']/div/div[1]"
        self.tools_and_trackers_xpath = "//div[@name='mainContent']/div/div[2]"

    def click_on_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()

    def click_on_heath_card(self):
        self.driver.find_element_by_xpath(self.health_card_xpath).click()

    def click_on_tools_and_trackers(self):
        self.driver.find_element_by_xpath(self.tools_and_trackers_xpath).click()
