import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pytest_framework.main_page import MainPage
from pytest_framework.search_page import SearchPage


class TestWeb:
    main_page: SearchPage = None

    def setup_method(self):
        self.main_page = MainPage()

    @pytest.mark.parametrize("keyword, name", yaml.safe_load(open("demo.yaml", 'r', encoding="utf-8")))
    def test_search_by_po_dd(self, keyword, name):
        assert self.main_page.search(keyword).get_name() == name

    def teardown_method(self):
        self.main_page.close()

