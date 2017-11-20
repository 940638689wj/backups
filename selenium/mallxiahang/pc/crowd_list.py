from package_manage import *

# 众筹列表
def crowd_list(driver):
	time.sleep(0.5)
	start = Start()
	driver.get('http://xh.dayang1.cn/crowdfunding/list')
	driver.find_element_by_css_selector('.show_tips .pic a').click()
	driver.find_element_by_partial_link_text('立即参与众筹').click()

	# 详情页面
	WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'integral')))
	driver.find_element_by_id('integral').click()
	driver.find_element_by_id('balancepaymentBtn').click()
	driver.find_element_by_css_selector('input[type=password]').send_keys(start.pay_password)
	driver.find_element_by_partial_link_text('确定').click()

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	crowd_list(driver)