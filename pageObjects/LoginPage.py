from selenium import webdriver


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"  # textboxların id leri ile bağlanırız
    button_login_xpath = "//button[@class='button-1 login-button']"  # inputların claslarını böyle alırız
    link_logout_linktext = "Logout"  # a etikeklerinin text'ini
    link_logout_xpath = "//a[normalize-space()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath", self.button_login_xpath).click()

    def clickLogout(self):
        # self.driver.find_element_by_link_text(self.link_logout_linktext).click()
        self.driver.find_element("xpath", self.link_logout_xpath).click()