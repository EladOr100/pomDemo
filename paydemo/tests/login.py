import configparser

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from paydemo.infra.infraFunc import WebDriverFactory
from paydemo.pages.loginPage import LoginPage
from paydemo.pages.homePage import HomePage
import HtmlTestRunner
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("TEST START")
        # config init
        cls.my_config_parser = configparser.ConfigParser()
        cls.my_config_parser.read("../configs/dataConf")
        cls.name = cls.my_config_parser.get("AUTH", "USERNAME")
        cls.password = cls.my_config_parser.get("AUTH", "PASSWORD")
        cls.home_url = cls.my_config_parser.get("DEFAULT", "HOMEURL")
        cls.data_table = cls.my_config_parser.get("XPATH", "DATATABLE")
        cls.web_driver = cls.my_config_parser.get("DRIVER", "WEBDRIVER")

        # driver init
        cls.driver_factory = WebDriverFactory(cls.web_driver)
        cls.driver = cls.driver_factory.getWebDriverInstance()
        # cls.driver = webdriver.Chrome(executable_path="../../drivers/chromedriver.exe")

    def test_login_valid(self):
        print('test start ')
        driver = self.driver
        driver.get(self.home_url)

        login = LoginPage(driver)
        assert driver.current_url == self.home_url
        login.enter_username(self.name)
        login.enter_password(self.password)
        login.press_login_btn()
        assert driver.current_url != self.home_url
        home_page = HomePage(driver)
        d = driver.find_element_by_id('panel_resizable_1_1')
        home_page.get_table_data()
        home_page.click_welcome()
        home_page.click_logout_link()
        print('test end')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("TEST END")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/orela/PycharmProjects/selniumInt/reports'))
