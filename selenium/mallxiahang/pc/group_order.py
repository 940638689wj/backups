from package_manage import *

# 团购列表
def group_order(driver):
	group_index = 1 #第几个团购商品

	time.sleep(0.5)
	start = Start()
	driver.get('http://xh.dayang1.cn/groupPurchase/list#')
	driver.find_elements_by_css_selector('.show_tips .pic a')[group_index - 1].click()
	driver.find_element_by_partial_link_text('立即抢购').click()

	# 详情页面
	WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'integral')))
	driver.find_element_by_id('integral').click()

	#是否自定义付款页面
	confirm = driver.find_element_by_id('balancepaymentBtn')
	start.custom_pay_info(driver, confirm)

	driver.find_element_by_css_selector('input[type=password]').send_keys(start.pay_password)
	driver.find_element_by_partial_link_text('确定').click()

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	group_order(driver)