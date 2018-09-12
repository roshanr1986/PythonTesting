
from selenium import webdriver

import unittest
from selenium.webdriver.common.by import By


class TestCase():



    def testWeblink(self):
        self.driver = webdriver.Chrome("C:\\Users\\pcadmin\\IdeaProjects\\PythonTesting\\Drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.mercurytravels.co.in/indian-holidays")
        h = HomePage(self.driver)



class HomePage(TestCase):

    def __init__(self, driver):
        self.driver = driver
        self.INTERNATIONAL_HOLIDAYS = (
            By.XPATH,
            "//a[@class='int_link font14' and @title='International Holidays' and text()='International Holidays")

    def clickon_international_holidays(self):
        self.driver.find_element(self.INTERNATIONAL_HOLIDAYS).click()
