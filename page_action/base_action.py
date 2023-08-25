from time import sleep
from typing import Union

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://reqres.in/"

    def find_element(self, locator, time=5) -> Union:
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator=locator))

    def check_element(self, locator) -> bool:
        try:
            self.find_element(locator=locator, time=5)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, locator):
        find_element = self.find_element(locator)
        find_element.click()

    def get_text_element(self, locator) -> str:
        sleep(2)
        find_element = self.find_element(locator=locator, time=5)
        return find_element.text

    def go_to_site(self):
        return self.driver.get(self.base_url)
