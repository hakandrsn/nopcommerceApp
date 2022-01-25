import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    usermail = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen().loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("deneme")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()  # ilgilen
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle2.png")  # location belirtir + ismini
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.warning("deneme")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.usermail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()

            assert False
