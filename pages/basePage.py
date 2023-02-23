import time
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium.webdriver.common.by import By
class Page(object):
    """
        Page基类，所有page都应该继承该类
    """
    def __init__(self, driver, base_url="http://www.baidu.com"):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30

    def find_element(self, *loc):
        WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located(loc))
        return self.driver.find_element(*loc)

    def input_text(self, loc, text):
        self.find_element(*loc).send_keys(text)

    def click(self, loc):
        self.find_element(*loc).click()

    def get_title(self):
        return self.driver.title

    def get_input_text(self, loc):
        time.sleep(2)
        return self.find_element(*loc).get_attribute('value')#获取input输入的文本值和获取元素中的文本内容