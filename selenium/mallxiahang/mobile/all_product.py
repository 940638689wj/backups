from package_manage import *

# 全部商品
def all_product(driver):
	time.sleep(0.5)
	start = Start()
	driver.get('http://xh.dayang1.cn/m/products/0.html')

	for x in range(3, 5):
		driver.find_elements_by_css_selector('#productListUl a')[x-1].click()
		driver.find_element_by_partial_link_text('加入购物车').click()
		time.sleep(0.5)
		driver.find_element_by_partial_link_text('确定').click()
		driver.back()

	driver.find_element_by_partial_link_text('购物车').click()
	WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '结算')))
	driver.find_element_by_partial_link_text('结算').click()

	# 详情页面
	sendType = driver.find_element_by_xpath(
			'//*[@id="page"]/div/div[4]/div/ul/li[1]/div[2]/select')
	time.sleep(0.5)
	Select(sendType).select_by_index(2)

	# 是否自定义付款页面
	confirm = driver.find_element_by_id('balancepaymentBtn')
	start.custom_pay_info(driver, confirm)

	driver.find_element_by_id('pwd-input').send_keys(start.pay_password)
	time.sleep(0.5)
	driver.find_element_by_xpath('//*[@id="J_ASSpec"]/div[2]/div[3]/div/div/a[1]').click()

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	all_product(driver)
