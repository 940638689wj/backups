from package_manage import *

# 团购列表
def group_order(driver):
	group_index = 1 # 第几个团购商品

	time.sleep(0.5)
	start=Start()
	driver.get('http://xh.dayang1.cn/m/groupPurchase/list')

	driver.find_elements_by_css_selector('.prd-list a')[group_index-1].click()
	driver.find_element_by_link_text('立即抢购').click()
	time.sleep(0.5)
	driver.find_element_by_link_text('下一步').click()

	# 详情页面
	driver.find_element_by_xpath('//*[@id="page"]/div/div[5]/div/ul/li/a/div[1]/div').click()
	# 是否自定义付款页面
	confirm = driver.find_element_by_id('balancepaymentBtn')
	start.custom_pay_info(driver, confirm)

	driver.find_element_by_id('pwd-input').send_keys(start.pay_password)

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	group_order(driver)