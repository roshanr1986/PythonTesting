from selenium import webdriver
import Test.property.property
import unittest


class CommonDriver(object):

    def create_driver(self, url):
        driver = webdriver.Chrome("C:\Users\pcadmin\IdeaProjects\PythonTesting\Drivers\chromedriver.exe")
        driver.maximize_window()
        driver.get(url)
        return driver
