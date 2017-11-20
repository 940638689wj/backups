from package_manage import *

# 提货券
def pickup(driver):
	time.sleep(0.5)
	start = Start()
	driver.get('http://xh.dayang1.cn/m/pickup/index')
	WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name=pickupcouponList]')))
	driver.find_element_by_css_selector('input[name=pickupcouponList]').click()
	driver.find_element_by_class_name('chk_item').click()
	driver.find_element_by_link_text('下一步').click()

	# 详情页面
	sendType = driver.find_element_by_id('expressId')
	time.sleep(0.5)
	Select(sendType).select_by_index(2)

	driver.find_element_by_xpath('//*[@id="useUserBalance"]/div[1]/div').click()
	driver.find_element_by_id('doSubmitOrder').click()


	driver.find_element_by_id('pwd-input').send_keys(start.pay_password)
	time.sleep(0.5)
	driver.find_element_by_id('confirmBalancePay').click()

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	pickup(driver)