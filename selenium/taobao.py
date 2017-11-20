from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,threading

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('https://login.taobao.com/member/login.jhtml')
# driver.find_element_by_id('J_Quick2Static').click()
# driver.find_element_by_id('TPL_username_1').send_keys('安之若素丶wj')
# driver.find_element_by_id('TPL_password_1').send_keys('8312057000m,')
# ActionChains(driver).drag_and_drop(driver.find_element_by_id('nc_1_n1z'), driver.find_element_by_id('J_Static2Quick')).perform()
# time.sleep(2)
# driver.find_element_by_id('J_SubmitStatic').click()
# WebDriverWait(driver, 50).until(EC.title_contains('detail.tmall.com'))
time.sleep(20)
driver.get('https://detail.tmall.com/item.htm?id=560792599586&_u=t2dmg8j26111')
while True:
	if driver.find_element_by_id('J_LinkBuy').is_displayed():
		driver.find_element_by_id('J_LinkBuy').click()
		break
	else:
		driver.refresh()

# [
# 	{
# 		'css_selector': '#id',
# 		'success': '1',
# 		'error': ['-1', '0', '9999']
# 	}
# ]

# def validate(params):
# 	for param in params:
# 		driver.find_element_by_css_selector(param['css_selector']).send_keys(param['success'])
