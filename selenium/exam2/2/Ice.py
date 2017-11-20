from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('http://lbdxs.dayang1.cn/admin/sa/login')

# 对于下拉框（Select标签）需要单独的处理方式
#org_select = driver.find_element_by_id('orgId')
#time.sleep(2)
#Select(org_select).select_by_value('5')
#org_select1 = driver.find_element_by_id('storeId')
#time.sleep(2)
#Select(org_select1).select_by_value('4')
driver.find_element_by_id('username').send_keys('admin')
driver.find_element_by_id('password').send_keys('admin')
driver.find_element_by_id('randomCode').send_keys('987654')
driver.find_element_by_class_name('loginbtn').click()
#driver.find_element_by_class_name('bui-menu-item menu-leaf').click()
ele_ifram = driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(1) > iframe')
driver.switch_to_frame(ele_ifram)
driver.find_element_by_css_selector('#bar-item-button1 > button').click()
#driver.find_element_by_id('primaryPicFileObj').click()
#driver.implicitly_wait(10)
#driver.find_element_by_id('primaryPicFileObj').click()
#driver.find_element_by_css_selector('#primaryPicFileObj').send_keys('D:\img\1.jpg')
driver.switch_to_default_content()
ele1_ifram = driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(2) > iframe')
driver.switch_to_frame(ele1_ifram)
driver.find_element_by_id('primaryPicFileObj').send_keys('D:\\img\\1.jpg')
driver.find_element_by_id('productName').send_keys('pingguo')
driver.find_element_by_id('productSubTitle').send_keys('hahaahahah')
#driver.find_element_by_id('categoryId').send_keys('hahaahahah')
org_select = driver.find_element_by_id('categoryId')
time.sleep(2)
Select(org_select).select_by_value('2')
org_select1 = driver.find_element_by_id('countType')
time.sleep(2)
Select(org_select1).select_by_value('1')
driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(4) > div > input').send_keys('5')
org_select1 = driver.find_element_by_id('weightStockCommonUnitId')
time.sleep(2)
Select(org_select1).select_by_value('1')
org_select1 = driver.find_element_by_id('measureStockCommonUnitId')
time.sleep(2)
Select(org_select1).select_by_value('5')

org_select1 = driver.find_element_by_id('transportTypeCd')
time.sleep(2)
Select(org_select1).select_by_value('1')
driver.find_element_by_css_selector('#Basic_Info_Form > div.prdbasic.clearfix > div.prd-colmain > div > div > div:nth-child(3) > div.panel-body > div:nth-child(8) > div > div > input').send_keys('苹果味道')
driver.find_element_by_css_selector('#allBarCode > div:nth-child(1) > div > input.control-text.barCode.bui-form-field').send_keys('666666')
driver.implicitly_wait(20)
driver.find_element_by_id('save').click()









#driver.find_element_by_id('search_product').send_keys('合味道')
#driver.find_element_by_class_name('deepbluebtn').click()
#driver.find_element_by_class_name('numinput').clear()
#driver.find_element_by_class_name('numinput').send_keys('2')
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			#[By.CLASS_NAME, 'toolbar'])).find_element_by_partial_link_text('单品折扣').click()
#driver.find_element_by_id('p_discount').send_keys('50')
#driver.find_element_by_class_name('layui-layer-btn0').click()
#driver.find_element_by_class_name('button').click()
#driver.find_element_by_id('receiverPrice').send_keys('17500')
#			[By.CLASS_NAME, 'payment'])).find_element_by_partial_link_text('现金支付').click()