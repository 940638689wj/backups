from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class Start(object):

	# login_name = '15005921012'  # 账号
	login_name = '18959262685'  # 账号
	passowrd = '123123'  # 密码
	pay_password = '123321'  # 支付密码

	# 是否自定义付款页面
	is_custom = False
	# is_custom = True

	def __init__(self):
		pass

	'''初始化配置 和 登录'''

	def config_driver(self, driver):
		driver.implicitly_wait(5)
		# driver.get('http://localhost:8080/account')
		driver.get('http://xh.dayang1.cn/account')
		# driver.maximize_window()

		# 登录
		driver.find_element_by_id('loginName').send_keys(self.login_name)
		driver.find_element_by_id('password').send_keys(self.passowrd)
		driver.find_element_by_id('verifyCode').send_keys('968574321')
		driver.find_element_by_id('doLogin').click()

	'''是否需要自定义付款页面'''

	def custom_pay_info(self, driver, confirm):

		if self.is_custom:
			WebDriverWait(driver, 100).until(EC.element_to_be_clickable(
				(By.CSS_SELECTOR, 'input[type=password]')))
		else:
			confirm.click()
