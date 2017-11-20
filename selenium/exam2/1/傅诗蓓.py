from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
def create_web(driver):
	driver.get('http://posxs.dayang1.cn/admin/pc/login')
	org_select = driver.find_element_by_id('orgId')
	# time.sleep(2)
	Select(org_select).select_by_value('6')
	md_select = driver.find_element_by_id('storeId')
	Select(md_select).select_by_value('16')
	port_select = driver.find_element_by_id('deviceId')
	Select(port_select).select_by_value('14')
	driver.find_element_by_id('username').send_keys('ww')
	driver.find_element_by_id('password').send_keys('123456')
	driver.find_element_by_id('randomCode').send_keys('987654')
	driver.find_element_by_id('sub').click()
	driver.find_element_by_id('search_product').send_keys('农夫山泉')
	driver.find_element_by_class_name('deepbluebtn').click()
	driver.find_element_by_class_name('numinput').send_keys('1')
	#driver.find_element_by_class_name('deepbluebtn').click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			[By.CLASS_NAME, 'toolbar'])).find_element_by_partial_link_text('单品折扣').click()
	#time.sleep(3)
	driver.find_element_by_id('p_discount').send_keys('90')
	driver.find_element_by_link_text('确定').click()
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			[By.CLASS_NAME, 'r'])).find_element_by_partial_link_text('结账').click()
	#driver.find_element_by_class_name('inputext').send_keys('10')
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			[By.CLASS_NAME, 'zk'])).find_element_by_class_name('inputext').send_keys('10')
	WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			[By.CLASS_NAME, 'payment'])).find_element_by_partial_link_text('现金支付').click()

driver = webdriver.Chrome()
driver.implicitly_wait(10)
create_web(driver)