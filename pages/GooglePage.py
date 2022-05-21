import time

from Locators.Locators import GooglePageLocators
from pages.BasePage import BasePage


class GooglePage(BasePage):

    def __init__(self, driver):
        self.locator = GooglePageLocators
        super(GooglePage, self).__init__(driver)
        self.driver = driver

    def search(self, keyword):
        self.find_element(*self.locator.SearchBox).clear()
        for ch in keyword:
            time.sleep(0.1)
            self.find_element(*self.locator.SearchBox).send_keys(ch)

        self.find_element(*self.locator.SearchBtn).click()
