class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_name = "loginid"
        self.password_textbox_name = "userpassword"
        self.login_class_name = 'ng-binding'

    def enter_username(self, username):
        self.driver.find_element_by_name(self.username_textbox_name).clear()
        self.driver.find_element_by_name(self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_class_name(self.login_class_name).click()
