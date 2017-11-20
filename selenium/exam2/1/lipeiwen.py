from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select 

def test(driver):
	driver.get('http://posxs.dayang1.cn/admin/pc/login')
	time.sleep(5)
	Select(driver.find_element_by_css_selector('#orgId')).select_by_index(6)
	Select(driver.find_element_by_css_selector('#storeId')).select_by_index(0)
	Select(driver.find_element_by_css_selector('#deviceId')).select_by_index(0)
	driver.find_element_by_css_selector('#username').send_keys('1')
	driver.find_element_by_css_selector('#password').send_keys('1')
	driver.find_element_by_css_selector('#randomCode').send_keys('987654')
	driver.find_element_by_css_selector('#sub').click()
	driver.find_element_by_css_selector('#search_product').send_keys('1234567890123001')
	driver.find_element_by_class_name('deepbluebtn').click()
	driver.find_element_by_class_name('numinput').click()
	driver.find_element_by_class_name('numinput').send_keys('2')
	driver.find_element_by_css_selector('body > div.pos-page > div.pos-footer > div.toolbar > ul > li:nth-child(2) > a > p').click()
	driver.find_element_by_id('p_discount').send_keys('50')
	driver.find_element_by_class_name('layui-layer-btn0').click()
	driver.find_element_by_link_text('结账').click()
	driver.find_element_by_id('receiverPrice').send_keys('10')
	driver.find_element_by_css_selector('#checkout > div > div.payment > ul.commonPayment > li:nth-child(1) > a').click()


if __name__ == '__main__':
	driver=webdriver.Chrome()
	driver.implicitly_wait(20)
	driver.get('http://posxs.dayang1.cn/admin/pc/login')
	test(driver)