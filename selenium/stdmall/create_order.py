from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time


# 全部商品
def create_order(driver):
	time.sleep(1)
	driver.get('http://localhost:8080/products/0.html')
	for x in range(0, 3):
		driver.find_elements_by_css_selector('#pr-list .show_tips')[x].click()
		time.sleep(1)
		driver.find_element_by_partial_link_text('加入购物车').click()
		driver.back()

	driver.find_element_by_partial_link_text('我的购物车').click()
	WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'buyNow')))
	time.sleep(0.5)
	driver.find_element_by_id('buyNow').click()

	# 详情页面
	time.sleep(1)
	driver.find_element_by_id('btnBuy').click()
	time.sleep(0.5)
	driver.find_element_by_partial_link_text('支付宝').click()

	# driver.find_element_by_link_text('余额支付').click()
	# driver.find_element_by_css_selector('#password').send_keys('123321')
	# driver.find_element_by_partial_link_text('确定').click()

if __name__=='__main__':
	driver = webdriver.Chrome()
	driver.implicitly_wait(10)
	driver.get('http://localhost:8080')
	driver.delete_cookie('JSESSIONID')
	driver.add_cookie({'name': 'JSESSIONID', 'value': 'E6CC6B119EA763D4F9A4DA5137364DF7'})
	for x in range(0,3):
		create_order(driver)
