from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pytest_framework.base_page import BasePage
from pytest_framework.search_page import SearchPage


class MainPage(BasePage):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('https://xueqiu.com/')

    def search(self, keyword):
        # SearchPage是类，返回SearchPage的实例对象
        element_input = self.find(By.NAME, 'q')
        element_input.clear()
        element_input.send_keys(keyword)
        element_input.send_keys(Keys.ENTER)

        return SearchPage(self.driver)

