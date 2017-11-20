from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

def creat_order(driver):
	driver.implicitly_wait(10)
	driver.get('http://posxs.dayang1.cn/admin/pc/login')
	time.sleep(2)
	
	Select(driver.find_element_by_css_selector('#orgId')).select_by_index(3)
	driver.find_element_by_css_selector('#username').send_keys('sy01')
	driver.find_element_by_css_selector('#password').send_keys('123456')
	driver.find_element_by_css_selector('#randomCode').send_keys('987654')
	driver.find_element_by_css_selector('#sub').click()

	driver.find_element_by_css_selector('#search_product').send_keys('174082641269283')
	driver.find_element_by_css_selector('body > div.pos-page > div.pos-container > div > div.facility > div > div.searchbtn > button').click()
	driver.find_element_by_css_selector('#selectTbody input').clear()
	driver.find_element_by_css_selector('#selectTbody > tr > td:nth-child(8) > input').send_keys('2')
	driver.find_element_by_css_selector('body > div.pos-page > div.pos-footer > div.toolbar > ul > li:nth-child(2) > a > p').click()
	driver.find_element_by_css_selector('#p_discount').send_keys('98')
	driver.find_element_by_link_text('确定').click() # 
	driver.find_element_by_css_selector('body > div.pos-page > div.pos-footer > div.info > div.r > a.button').click()
	driver.find_element_by_css_selector('#receiverPrice').send_keys('200')
	driver.find_element_by_link_text('现金支付').click() # 




if __name__ == '__main__':
	driver = webdriver.Chrome()
	creat_order(driver)