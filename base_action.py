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

    #def find_elements(self, locator, time=5) -> Union:
    #    return WebDriverWait(self.driver, time).until(
    #        expected_conditions.presence_of_all_elements_located(locator=locator))

    def check_element(self, locator) -> bool:
        try:
            self.find_element(locator=locator, time=10)
        except NoSuchElementException:
            return False
        return True

    def click_element(self, locator):
        find_element = self.find_element(locator)
        find_element.click()

    def get_text_element(self, locator) -> str:
        sleep(2)
        find_element = self.find_element(locator=locator, time=15)
        return find_element.text

    def go_to_site(self):
        return self.driver.get(self.base_url)

    #def enter_text(self, locator, text):
    #    find_element = self.find_element(locator)
    #   find_element.click()
    #   find_element.send_keys(text)

    # Парсинг данных из таблицы в объект и упаковка всех объектов в список
    #def parse_table(self, locator_row) -> list[TransactionJournal, ...]:
    #    parse_table = []
    #   len_row = len(self.find_elements(locator=locator_row))
    #    len_cell = len(self.find_elements(locator=(locator_row[0], locator_row[1] + '[1]//td')))
    #    for row in range(0, len_row):
    #        parse_row = []
    #        for cell in range(0, len_cell):
    #            locator = (locator_row[0],
    #                       locator_row[1] + '[' + str(row + 1) + ']//td[' + str(cell + 1) + ']')
    #            parse_row.append(self.get_text_element(locator=locator))
    #        parse_table.append(TransactionJournal.from_ui(parse_row[0], parse_row[1], parse_row[2]))
    #    return parse_table