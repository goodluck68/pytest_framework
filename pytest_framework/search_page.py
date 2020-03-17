from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pytest_framework.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.find(By.CSS_SELECTOR, '.search__stock__bd span').text

    def search(self, keyword):
        element_input = self.find(By.NAME, 'q')
        element_input.clear()
        element_input.send_keys(keyword)
        element_input.send_keys(Keys.ENTER)

        return self


