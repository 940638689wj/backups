from selenium import webdriver
import time
import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

def add_product(driver):
	time.sleep(1)
	driver.get('http://lbdxs.dayang1.cn/admin/sa/login')
	# 登录
	driver.find_element_by_id('username').send_keys('yu')
	driver.find_element_by_id('password').send_keys('123456')
	driver.find_element_by_id('randomCode').send_keys('987654')
	driver.find_element_by_class_name('loginbtn').click()

	# driver.delete_all_cookies()
	# driver.add_cookie({'name':'JSESSIONID','value':'B6BC3B1F7C9'})
	# time.sleep(1)
	# driver.refresh()

	# 新建商品
	# driver.find_element_by_class_name('product:add').click()
	driver.find_element_by_partial_link_text('新建商品').click()

	# 跳转至框架
	driver.switch_to_frame(driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(2) > iframe'))


	# 商品图片
	driver.find_element_by_id('primaryPicFileObj').send_keys('D:\\img\\1.jpg')

	# 商品名称、描述
	driver.find_element_by_id('productName').send_keys('RIO鸡尾酒')
	driver.find_element_by_id('productSubTitle').send_keys('RIO鸡尾酒 瓶装')

	# 商品类目
	Select(driver.find_element_by_id("categoryId")).select_by_index(4)

	# 计算类型
	Select(driver.find_element_by_id("countType")).select_by_index(0)

	# 容量
	driver.find_element_by_name('productWeight').send_keys('300')
	Select(driver.find_element_by_id("weightStockCommonUnitId")).select_by_index(3)

	# 计量单位
	Select(driver.find_element_by_id("measureStockCommonUnitId")).select_by_index(7)

	# 存储方式
	Select(driver.find_element_by_id("transportTypeCd")).select_by_index(1)

	# 口味
	driver.find_element_by_name('tastes').send_keys('混合')

	# 条码
	# driver.find_element_by_name('barCode').send_keys('1584236547808')
	driver.find_element_by_name('barCode').send_keys(str(random.randint(1000,9999)))

	# 下一步
	# driver.find_element_by_id('save').click()

	# # 跳出框架至另一个框架
	# driver.switch_to_default_content()
	# driver.switch_to_frame(driver.find_element_by_css_selector('#J_productTab > div > div.tab-content-container > div:nth-child(3) > iframe'))

	# # 保存
	# driver.find_element_by_css_selector('#D_Form > div.row.form-actions.actions-bar > div > button').click()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	add_product(driver)
