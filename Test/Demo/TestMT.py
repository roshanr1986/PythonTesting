from selenium import webdriver
from selenium.webdriver.common.by import By
from Test.implementations.commonDriver import CommonDriver
from Test.PageObjects.HomePage import HomePage
from Test.PageObjects.MtHomePge import MtHomePage
from Test.property.property import property
import unittest


class TestMT(unittest.TestCase):

    def test_mt(self):
        global driver
        global home
        commondriver = CommonDriver()
        driver = commondriver.create_driver(property.MT_url)
        home = MtHomePage(driver)
        # driver = webdriver.Chrome("C:\\Users\\pcadmin\\IdeaProjects\\PythonTesting\\Drivers\\chromedriver.exe")
        # driver.get("https://www.mercurytravels.co.in/indian-holidays")
        self.click_on_link(home.initiate_international_holiday())

        # SEARCH_BUTTON = (By.XPATH, '//input[@name="btnK" and @value="Google Search"]')

    def click_on_link(self, element):
        self.driver.find_element(element).click()


if __name__ == '__main__':
    unittest.main()
