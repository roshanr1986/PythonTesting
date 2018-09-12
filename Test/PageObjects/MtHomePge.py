from selenium.webdriver.common.by import By


class MtHomePage(object):


    def __init__(self, driver):
        self.driver = driver

    def initiate_international_holiday(self):
        INTERNATIONAL_HOLIDAYS_LINK = (By.XPATH, '//li//a[@class="int_link font14" and @title="International Holidays" and text()="International Holidays"]')
        return INTERNATIONAL_HOLIDAYS_LINK





