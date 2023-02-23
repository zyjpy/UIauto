# searchPage.py 代码如下
# _*_ coding:utf-8 _*_

__author__ = '苦叶子'

import sys
import time

from selenium.webdriver.common.by import By
from pages.basePage import Page
# 百度搜索page
class SearchPage(Page):
    # 元素集

    # 搜索输入框
    search_input = (By.ID,'kw')
    # 百度一下 按钮
    search_button = (By.ID,'su')
    clear_button = (By.CSS_SELECTOR,'.quickdelete')

    def gotoBaiduHomePage(self):

        self.driver.get(self.base_url)

    def input_search_text(self, text="开源优测"):

        self.input_text(self.search_input, text)

    def click_search_btn(self):

        self.click(self.search_button)
        time.sleep(3)
        self.click(self.clear_button)
        time.sleep(3)
        print(self.get_input_text(self.search_button))