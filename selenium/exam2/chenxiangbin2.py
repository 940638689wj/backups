from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# def creat_order(driver):
# 	driver.implicitly_wait(10)
# 	driver.get('http://posxs.dayang1.cn/admin/pc/login')
# 	time.sleep(2)
# 	Select(driver.find_element_by_css_selector('#orgId')).select_by_index(3)
# 	driver.find_element_by_css_selector('#username').send_keys('sy01')
# 	driver.find_element_by_css_selector('#password').send_keys('123456')
# 	driver.find_element_by_css_selector('#randomCode').send_keys('987654')
# 	driver.find_element_by_css_selector('#sub').click()
# 	driver.find_element_by_css_selector('#search_product').send_keys('174082641269283')
# 	driver.find_element_by_css_selector('body > div.pos-page > div.pos-container > div > div.facility > div > div.searchbtn > button').click()
# 	driver.find_element_by_css_selector('#selectTbody > tr > td:nth-child(8) > input').clear()
# 	driver.find_element_by_css_selector('#selectTbody > tr > td:nth-child(8) > input').send_keys('2')
# 	driver.find_element_by_css_selector('body > div.pos-page > div.pos-footer > div.toolbar > ul > li:nth-child(2) > a > p').click()
# 	driver.find_element_by_css_selector('#p_discount').send_keys('98')
# 	driver.find_element_by_link_text('确定').click()
# 	driver.find_element_by_css_selector('body > div.pos-page > div.pos-footer > div.info > div.r > a.button').click()
# 	driver.find_element_by_css_selector('#receiverPrice').send_keys('200')
# 	driver.find_element_by_link_text('现金支付').click()




# if __name__ == '__main__':
# 	driver = webdriver.Chrome()
# 	creat_order(driver)
	
def creat_goods(driver):
	driver.get('http://lbdxs.dayang1.cn/admin/sa/login')
	driver.implicitly_wait(10)
	driver.find_element_by_css_selector('#username').send_keys('admin')
	driver.find_element_by_css_selector('#password').send_keys('admin')
	driver.find_element_by_css_selector('#randomCode').send_keys('987654')
	driver.find_element_by_css_selector('button').click()
	driver.find_element_by_link_text('新建商品').click()
	time.sleep(2)
	driver.switch_to_frame(driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(2) > iframe'))
	driver.find_element_by_css_selector('#primaryPicFileObj').send_keys('d:\\img\\1.jpg')
	driver.find_element_by_css_selector('#productName').send_keys('商品名称')
	driver.find_element_by_css_selector('#productSubTitle').send_keys('商品描述')
	Select(driver.find_element_by_css_selector('#categoryId')).select_by_index(1)
	Select(driver.find_element_by_css_selector('#brandId')).select_by_index(1)
	driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(1) > div > input').send_keys('spmc')
	driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(2) > div > input').send_keys('360')
	Select(driver.find_element_by_css_selector('#countType')).select_by_index(0)
	driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(4) > div > input').send_keys('100')
	Select(driver.find_element_by_css_selector('#weightStockCommonUnitId')).select_by_index(1)
	Select(driver.find_element_by_css_selector('#measureStockCommonUnitId')).select_by_index(1)
	Select(driver.find_element_by_css_selector('#transportTypeCd')).select_by_index(1)
	driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(8) > div > div > input').send_keys('原味')
	driver.find_element_by_css_selector('#allBarCode > div:nth-child(1) > div > input.control-text.barCode.bui-form-field').send_keys('2017102617017')
	driver.find_element_by_css_selector('#save').click()
	# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			# [By.CSS_SELECTOR, '#save'])).find_element_by_css_selector('#save').click()
	time.sleep(5)
	driver.switch_to_default_content()
	driver.switch_to_frame(driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(3) > iframe'))
	driver.find_element_by_css_selector('#D_Form > div.row.form-actions.actions-bar > div > button').click()
	# WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
	# 		[By.CSS_SELECTOR, '#D_Form > div.row.form-actions.actions-bar > div > button'])).find_element_by_link_text('保存').click()
	
	






if __name__ == '__main__':
	driver = webdriver.Chrome()
	creat_goods(driver)




