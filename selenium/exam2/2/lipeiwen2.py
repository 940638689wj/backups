from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select 

def test(driver):
	driver.get('http://lbdxs.dayang1.cn/admin/sa/login')
	driver.find_element_by_id('username').send_keys('admin')
	driver.find_element_by_id('password').send_keys('admin')
	driver.find_element_by_id('randomCode').send_keys('987654')
	driver.find_element_by_class_name('loginbtn').click()

	#pow=driver.find_element_by_xpath('//*[@id="J_productTab"]/div/div[2]/div[2]/iframe')
	driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="J_productTab"]/div/div[2]/div[1]/iframe'))
	driver.find_element_by_xpath('//*[@id="bar-item-button1"]/button').click()
	driver.switch_to_default_content()
	driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="J_productTab"]/div/div[2]/div[2]/iframe'))
	#driver.find_element_by_css_selector('#primaryPicFileObj').click()
	driver.find_element_by_css_selector("#primaryPicFileObj").send_keys(r'd:\img\1.jpg')
	driver.find_element_by_id('productName').send_keys('yirui')
	driver.find_element_by_id('productSubTitle').send_keys('yirui')
	Select(driver.find_element_by_css_selector('#categoryId')).select_by_index(1)
	Select(driver.find_element_by_css_selector('#brandId')).select_by_index(0)
	Select(driver.find_element_by_css_selector('#countType')).select_by_index(1)
	driver.find_element_by_xpath('//*[@id="Basic_Info_Form"]/div[1]/div[2]/div/div/div[2]/div[2]/div[4]/div/input').send_keys('1')
	Select(driver.find_element_by_css_selector('#weightStockCommonUnitId')).select_by_index(1)
	Select(driver.find_element_by_css_selector('#transportTypeCd')).select_by_index(1)
	driver.find_element_by_xpath('//*[@id="Basic_Info_Form"]/div[1]/div[2]/div/div/div[2]/div[2]/div[8]/div/div/input').send_keys('wu')
	driver.find_element_by_xpath('//*[@id="allBarCode"]/div[1]/div/input[3]').send_keys('123456758478')
	#time.sleep(3)
	driver.find_element_by_id('save').click()
	driver.switch_to_default_content()
	driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="J_productTab"]/div/div[2]/div[3]/iframe'))
	driver.find_element_by_xpath('//*[@id="D_Form"]/div[2]/div/button').click()



	



if __name__ == '__main__':
	driver=webdriver.Chrome()
	driver.implicitly_wait(20)
	driver.get('http://lbdxs.dayang1.cn/admin/sa/login')
	test(driver)