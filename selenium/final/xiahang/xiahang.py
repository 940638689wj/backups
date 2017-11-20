from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def create_order(driver):
	time.sleep(1)
	driver.get('http://xh.dayang1.cn/index.html')
	product_list = ['瓜子（配送）', '农夫山泉']
	for product in product_list:
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			[By.CSS_SELECTOR, '.navigation'])).find_element_by_link_text('全部商品').click()
		driver.find_element_by_link_text(product).click()
		driver.find_element_by_id('count').clear()
		driver.find_element_by_id('count').send_keys('2')
		driver.find_element_by_partial_link_text('加入购物车').click()

	driver.find_element_by_partial_link_text('我的购物车').click()
	driver.find_element_by_id('buyNow').click()
	Select(driver.find_element_by_css_selector('#main .formList select')).select_by_index(1)
	driver.find_element_by_id('btnBuy').click()
	driver.find_element_by_css_selector('#payPassword > div:nth-child(1) > div:nth-child(2) > div.bd > input').send_keys('123456')
	driver.find_element_by_link_text('确定').click()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.implicitly_wait(20)
	driver.get('http://xh.dayang1.cn/login')
	driver.find_element_by_id('loginName').send_keys('18065980762')
	driver.find_element_by_id('password').send_keys('123456q')
	driver.find_element_by_id('verifyCode').send_keys('968574321')
	driver.find_element_by_id('doLogin').click()
	for x in range(1,5):
		create_order(driver)
