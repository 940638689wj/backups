from selenium import webdriver
import time

def iframe_test(driver):
	driver.get('file:///E:/sublimeWorkspace/selenium/iframe/iframe_test.html')

	# 查找出nav的数量 和 所有的nav的内容
	# ele_list = driver.find_elements_by_css_selector('#tab .nav')
	# print(len(ele_list))
	# for ele in ele_list:
	# 	print(ele.text)


	# 定位到iframe内的元素
	driver.find_element_by_css_selector('#tab .nav').click()
	# time.sleep(2)

	# driver.switch_to_frame('ifr') # 通过id进入iframe
	ele_ifram = driver.find_element_by_css_selector('#content iframe')
	driver.switch_to_frame(ele_ifram)
	ele_text = driver.find_element_by_id('text')
	print(ele_text.text)
	time.sleep(2)
	driver.switch_to_default_content()
	driver.find_elements_by_css_selector('#tab .nav')[1].click()


if __name__ == '__main__':
	driver = webdriver.Chrome()
	iframe_test(driver)
