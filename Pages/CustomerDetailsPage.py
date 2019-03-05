# from selenium import webdriver
class CustomerDetailsPage:
    def __init__(self, driver):
        self.driver = driver

        self.customer_text_xpath = "//*[@id='printSectionId']/div[1]/div/div/div[1]/div/p/strong/small/br"
        self.customer_detail_link = "/html/body/div/div[3]/div/div/div[3]/div/ul/li[2]/div[1]"
        self.health_card_detail_text = "//*[@id='myModal']/div/div/div[1]/h4"

    def validate_customer_name(self, name):
        customer_name = self.driver.find_element_by_xpath(self.customer_text_xpath).text
        assert customer_name in name

    def click_customer_name(self):
        self.driver.find_element_by_xpath(self.customer_detail_link).click()

    def validate_health_card_detail_dialogue_box(self, name):
        health_card_detail_text = self.driver.find_element_by_xpath(self.health_card_detail_text).text
        print(health_card_detail_text)
        assert health_card_detail_text in name
