# -*- coding:utf-8 -*-
from selenium import webdriver
import time

def create_web(driver):
	driver.get('http://www.baidu.com')
	# driver.find_element_by_name('tj_trnews').click()
	country_list = ['中国', '美国', '日本']
	for country in country_list:
		driver.find_element_by_id('kw').send_keys(country)
		driver.find_element_by_id('su').click()
		time.sleep(3)
		driver.find_element_by_id('kw').clear()

	driver.find_element_by_css_selector('#kw')
	time.sleep(3)
	# driver.find_element_by_link_text('下一页').click()
	driver.find_element_by_partial_link_text('下一页').click()


	# driver.find_element_by_css_selector('#kw').send_keys('中国')
	# driver.find_element_by_css_selector('.s_btn').click()
	# time.sleep(3)

	# a_text = driver.find_element_by_tag_name('a').text
	# a_tag_list = driver.find_elements_by_tag_name('a')

	# tab_list = driver.find_elements_by_css_selector('#s_tab a')

	# for tab in tab_list:
	# 	print(tab.text)
	# a_tag_list = driver.find_elements_by_css_selector('a')
	# for a_tag in a_tag_list:
	# 	print(a_tag.text)
	# print(a_text_list[0].text)
	


	driver.find_element_by_id('kw').send_keys('美国')
	driver.find_element_by_id('su').click()
	time.sleep(3)
	driver.find_element_by_id('kw').clear()


	driver.find_element_by_id('kw').send_keys('日本')
	driver.find_element_by_id('su').click()
	time.sleep(20)
	driver.find_element_by_id('kw').clear()

driver = webdriver.Chrome()
create_web(driver)
# driver.find_element_by_id('kw')
