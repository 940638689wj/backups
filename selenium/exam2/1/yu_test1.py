from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

def pos_order(driver):
	time.sleep(1)
	driver.get('http://posxs.dayang1.cn/admin/pc/login')
	# 登录
	time.sleep(1)
	Select(driver.find_element_by_id("orgId")).select_by_index(0)
	Select(driver.find_element_by_id("storeId")).select_by_index(0)
	Select(driver.find_element_by_id("deviceId")).select_by_index(0)
	driver.find_element_by_id('username').send_keys('yu1')
	driver.find_element_by_id('password').send_keys('123456')
	driver.find_element_by_id('randomCode').send_keys('987654')
	driver.find_element_by_id('sub').click()

	time.sleep(1)
	# 查找商品、增加数量
	driver.find_element_by_id('search_product').send_keys('农夫山泉')
	driver.find_element_by_class_name('deepbluebtn').click()
	time.sleep(1)
	driver.find_element_by_class_name('numinput').clear()
	driver.find_element_by_class_name('numinput').send_keys('2')

	# 单品折扣
	driver.find_element_by_partial_link_text('单品折扣').click()
	driver.find_element_by_id('p_discount').send_keys('80')
	driver.find_element_by_class_name('layui-layer-btn0').click()

	# 结账
	driver.find_element_by_class_name('button').click()

	# 收款、现金支付
	driver.find_element_by_id('receiverPrice').send_keys('20')
	driver.find_element_by_partial_link_text('现金支付').click()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	pos_order(driver)
