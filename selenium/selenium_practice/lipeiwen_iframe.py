from selenium import webdriver
import time
def ifr_test(driver):
	driver.get('https://mail.qq.com/')
	ele_ifram1 = driver.find_element_by_css_selector('#login iframe')
	driver.switch_to_frame(ele_ifram1)
	driver.find_element_by_link_text('帐号密码登录').click()
	time.sleep(2)
	driver.find_element_by_id('u').send_keys('1022167917')
	driver.find_element_by_id('p').send_keys('LPW.941210.')
	driver.find_element_by_id('login_button').click()
	driver.switch_to_default_content()
	time.sleep(3)
	ele_ifram2=driver.find_element_by_css_selector('#mainFrameContainer iframe')
	driver.switch_to_frame(ele_ifram2)
	name=driver.find_element_by_xpath('//*[@id="TodayInBox"]/li[3]').text
	print(name)

if __name__ == '__main__':
	driver = webdriver.Chrome()
	ifr_test(driver)