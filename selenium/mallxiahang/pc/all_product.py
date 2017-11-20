from package_manage import *

# 全部商品
def all_product(driver):
	time.sleep(0.5)
	start = Start()
	driver.get('http://xh.dayang1.cn/products/0.html')
	for x in range(1, 3):
	  driver.find_elements_by_css_selector('.dl-name a')[x - 1].click()
	  driver.find_element_by_partial_link_text('加入购物车').click()
	  driver.back()

	driver.find_element_by_partial_link_text('我的购物车').click()
	WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'buyNow')))
	time.sleep(0.5)
	driver.find_element_by_id('buyNow').click()

	# 详情页面
	sendType = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[5]/div[2]/div[1]/div[2]/select')
	time.sleep(0.5)
	Select(sendType).select_by_index(2)

	# 是否自定义付款页面
	confirm = driver.find_element_by_id('btnBuy')
	start = Start()
	start.custom_pay_info(driver, confirm)

	driver.find_element_by_css_selector('input[type=password]').send_keys(start.pay_password)
	driver.find_element_by_partial_link_text('确定').click()

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	for x in range(1,10):
		all_product(driver)
