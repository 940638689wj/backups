from package_manage import *

# 提货券
def pickup(driver):
	time.sleep(0.5)
	start = Start()
	driver.get('http://xh.dayang1.cn/pickup/index.html')
	WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.LINK_TEXT, '选此套餐')))
	driver.find_element_by_link_text('选此套餐').click()

	# 详情页面
	sendType = driver.find_element_by_id('expressId')
	time.sleep(0.5)
	Select(sendType).select_by_index(2)
	driver.find_element_by_id('useUserBalance').click()
	driver.find_element_by_id('doSubmitOrder').click()
	driver.find_element_by_css_selector('input[type=password]').send_keys(start.pay_password)
	driver.find_element_by_partial_link_text('确定').click()

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	pickup(driver)