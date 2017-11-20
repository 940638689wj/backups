from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
# driver.maximize_window()

#强制等待
# time.sleep(2) 

# 隐式等待 全局仅需设置一次
driver.implicitly_wait(20)

# driver.get('file:///E:/sublimeWorkspace/selenium/iframe/display_test.html')
driver.get('file:///E:/sublimeWorkspace/selenium/iframe/display_test.html')
driver.find_element_by_id('menu_content').click()
# print(text)