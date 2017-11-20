from package_manage import *

# 众筹列表
def crowd_list(driver):
	time.sleep(0.5)
	start = Start()
	driver.get('http://xh.dayang1.cn/m/crowdfunding/list')

	driver.find_element_by_css_selector('#productListUl a').click()
	driver.find_element_by_link_text('立即参与众筹').click()

	# 详情页面
	balance = '//*[@id="page"]/div/div[2]/div/ul/li/a/div[1]/div'
	WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, balance)))
	driver.find_element_by_xpath(balance).click()
	driver.find_element_by_id('balancepaymentBtn').click()
	driver.find_element_by_id('pwd-input').send_keys(start.pay_password)

if __name__=='__main__':
	driver = webdriver.Chrome()
	Start().config_driver(driver)
	crowd_list(driver)