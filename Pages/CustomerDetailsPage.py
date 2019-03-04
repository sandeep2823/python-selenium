# from selenium import webdriver
class CustomerDetailsPage:
    def __init__(self, driver):
        self.driver = driver

        self.customer_text_xpath = "//*[@id='printSectionId']/div[1]/div/div/div[1]/div/p/strong/small/br"

    def validate_customer_name(self, name):
        customer_name = self.driver.find_element_by_xpath(self.customer_text_xpath).text
        assert customer_name in name
