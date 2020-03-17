from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pytest_framework.main_page import MainPage
from pytest_framework.search_page import SearchPage


class TestWeb:
    main_page: SearchPage = None

    # @classmethod
    # def setup_class(cls):
    #     cls.main_page = MainPage()

    def setup_method(self):
        self.main_page = MainPage()

    def test_search_by_po_sogo(self):
        """
        1. MainPage()对象调用search方法搜索"sogo"，返回SearchPage()对象
        2. SearchPage()对象再调用它的get_name方法，查看名字是否是"搜狗"
        """
        assert self.main_page.search('sogo').get_name() == "搜狗"

    def test_search_by_po_alibaba(self):
        assert self.main_page.search('alibaba').get_name() == "阿里巴巴"

