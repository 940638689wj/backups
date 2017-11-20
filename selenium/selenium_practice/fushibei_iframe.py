from selenium import webdriver
import time
def create_web():
	driver = webdriver.Chrome()
	driver.get('https://mail.qq.com')
	driver.switch_to_frame('login_frame')
	driver.find_element_by_css_selector('#switcher_plogin').click()
	driver.find_element_by_id('u').send_keys('467280813')
	driver.find_element_by_id('p').send_keys('fssy1184260603.')
	driver.find_element_by_css_selector('#login_button').click()
	time.sleep(5)
	driver.switch_to_frame('mainFrame')
	num_list = driver.find_elements_by_css_selector('#TodayInBox > li.mailinfo1.t_left2 a')
	for num in num_list:
		print(num.text)
	print(num)
create_web()