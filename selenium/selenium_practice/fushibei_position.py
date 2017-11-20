from selenium import webdriver
import time

def create_web():
	driver = webdriver.Chrome()
	driver.get('http://www.baidu.com')
	driver.find_element_by_css_selector('#u1 > a:nth-child(5)').click()
	driver.find_element_by_css_selector('#wd1').send_keys('selenium')
	driver.find_element_by_css_selector('#tb_header_search_form > span.search_btn_wrap.search_btn_enter_ba_wrap > a').click()
	num = driver.find_element_by_class_name('card_menNum').text
	print(num)
	tz = driver.find_element_by_class_name('card_infoNum').text
	print(tz)
	page_list = driver.find_elements_by_css_selector('div.threadlist_title.pull_left.j_th_tit a')
	for page in page_list:
		print(page.text)
	


create_web()