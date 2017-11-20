# -*- coding:utf-8 -*-
from selenium import webdriver
import time

def create_web(driver):
	driver.get('http://www.baidu.com')
	
	# 各种定位方式
	driver.find_element_by_id('kw').send_keys('selenium')
	driver.find_element_by_class_name('s_ipt').send_keys('a')
	driver.find_element_by_tag_name('input')
	driver.find_element_by_name('wd').send_keys('selenium')
	driver.find_element_by_css_selector('input[name=w`d]').send_keys('a')
	selected_tab_name = driver.find_element_by_css_selector('#s_tab b').text
	print(selected_tab_name)
	time.sleep(3)
	# driver.find_element_by_css_selector('#page > a:nth-child(4) > span.pc').click()
	driver.find_element_by_css_selector('#wrapper_wrapper .c-title-en a').click()
	driver.find_element_by_xpath('//*[@id="kw"]').send_keys('xpath')
	driver.find_element_by_link_text('下一页').click()
	driver.find_element_by_partial_link_text('下一页').click()



driver = webdriver.Chrome()
create_web(driver)
# driver.find_element_by_id('kw')
