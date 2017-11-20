from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('http://posxs.dayang1.cn/admin/pc/login')
driver.get('http://posxs.dayang1.cn/admin/pc/login')

# 对于下拉框（Select标签）需要单独的处理方式
org_select = driver.find_element_by_id('orgId')
time.sleep(2)
Select(org_select).select_by_value('5')
org_select1 = driver.find_element_by_id('storeId')
time.sleep(2)
Select(org_select1).select_by_value('4')
driver.find_element_by_id('username').send_keys('Iceblue')
driver.find_element_by_id('password').send_keys('123456')
driver.find_element_by_id('randomCode').send_keys('987654')
driver.find_element_by_id('sub').click()
driver.find_element_by_id('search_product').send_keys('合味道')
driver.find_element_by_class_name('deepbluebtn').click()
driver.find_element_by_class_name('numinput').clear()
driver.find_element_by_class_name('numinput').send_keys('2')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			[By.CLASS_NAME, 'toolbar'])).find_element_by_partial_link_text('单品折扣').click()
# driver.find_element_by_partial_link_text('单品折扣').click()
driver.find_element_by_id('p_discount').send_keys('50')
driver.find_element_by_class_name('layui-layer-btn0').click()
driver.find_element_by_class_name('button').click()
driver.find_element_by_id('receiverPrice').send_keys('17500')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			[By.CLASS_NAME, 'payment'])).find_element_by_partial_link_text('现金支付').click()






