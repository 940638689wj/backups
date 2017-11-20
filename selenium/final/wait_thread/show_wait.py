from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20) # 只检测标签元素的出现和消失 显示隐藏不触发
# driver.get('http://www.baidu.com')
# WebDriverWait(driver,10).until(EC.element_to_be_clickable([By.CSS_SELECTOR, '#kw'])).send_keys('a')

driver.get('file:///E:/sublimeWorkspace/selenium/iframe/display_test.html')
WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable([By.CSS_SELECTOR, '#menu_content']))

text = driver.find_element_by_css_selector('#menu_content').text
print(text)

# time.sleep(10)
# driver.close()