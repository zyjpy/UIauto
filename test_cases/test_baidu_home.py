# testSearchPage.py代码如下
# _*_ coding:utf-8 _*_

__author__ = '苦叶子'

import unittest
import sys
sys.path.append('.') 
from selenium import webdriver
from pages.searchPage import SearchPage
from logger import Logger
mylogger = Logger(logger='TestBaidu').getlog()


# 百度搜索测试
class TestSearchPage(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        
    def testSearch(self):
            driver = self.driver
            # 百度网址
            url = "http://www.baidu.com"
            # 搜索文本
            text = "开源优测"
            # 期望验证的标题
            assert_title = "开源优测_百度搜索"
            print (assert_title)
            
            search_Page = SearchPage(driver, url)
            
            # 启动浏览器，访问百度首页
            mylogger.info("启动浏览器，访问百度首页")
            search_Page.gotoBaiduHomePage()
            
            # 输入 搜索词
            mylogger.info("输入 搜索词")
            search_Page.input_search_text(text)
            
            # 单击 百度一下 按钮进行搜索
            mylogger.info("单击 百度一下 按钮进行搜索")
            search_Page.click_search_btn()
            # 验证标题
            mylogger.info("验证标题")
            # self.assertEqual(text,"水分子","导入作品失败")
            self.assertEqual(search_Page.get_title(), assert_title)
            print("hello")
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()