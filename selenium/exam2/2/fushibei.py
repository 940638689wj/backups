from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def create_web(driver):

	driver.get('http://lbdxs.dayang1.cn/admin/sa/login')
	#driver.maximize_window()
	#driver.implicitly_wait(20)
	driver.find_element_by_id('username').send_keys('admin')
	driver.find_element_by_id('password').send_keys('admin')
	driver.find_element_by_id('randomCode').send_keys('987654')
	driver.find_element_by_class_name('loginbtn').click()
	ele_ifram = driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(1) > iframe')
	driver.switch_to_frame(ele_ifram)
	driver.find_element_by_css_selector('#bar-item-button1 > button').click()
	driver.switch_to_default_content()
	sle_ifram = driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(2) > iframe')
	driver.switch_to_frame(sle_ifram)
	#WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			#[By.CLASS_NAME, 'prd-upload-icon'])).send_keys('d:\\img\\1.jpg')
	driver.find_element_by_id('primaryPicFileObj').send_keys('D:\\img\\1.jpg')
	driver.find_element_by_id('productName').send_keys('德芙巧克力')
	driver.find_element_by_id('productSubTitle').send_keys('丝滑好吃')
	org_select = driver.find_element_by_id('categoryId')
	# time.sleep(2)
	Select(org_select).select_by_value('4')
	num_select = driver.find_element_by_id('countType')
	# time.sleep(2)
	Select(num_select).select_by_value('1')
	driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(4) > div > input').send_keys('50')
	weight_select = driver.find_element_by_id('weightStockCommonUnitId')
	# time.sleep(2)
	Select(weight_select).select_by_value('1')
	mea_select = driver.find_element_by_id('measureStockCommonUnitId')
	# time.sleep(2)
	Select(mea_select).select_by_value('5')
	tra_select = driver.find_element_by_id('transportTypeCd')
	# time.sleep(2)
	Select(tra_select).select_by_value('1')
	driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(8) > div > div > input').send_keys('原味')
	# driver.find_element_by_css_selector('#allBarCode > div:nth-child(1) > div > input.control-text.barCode.bui-form-field').send_keys('68445441125980')
	driver.find_element_by_css_selector('#allBarCode > div:nth-child(1) > div > input.barCodeClassType.bui-form-field-radio.bui-form-check-field.bui-form-field.bui-form-field-radio-hover.bui-form-check-field-hover.bui-form-field-hover').click()
	# time.sleep(3)
	driver.find_element_by_id('save').click()
	#WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			#[By.CSS_SELECTOR, '#Basic_Info_Form > div.row.actions-bar > dive'])).find_element_by_partial_link_text('下一步').click()

driver = webdriver.Chrome()
driver.implicitly_wait(10)
create_web(driver)