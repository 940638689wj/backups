from selenium import webdriver
import time

def create_web():
	driver = webdriver.Chrome()
	driver.maximize_window()
	driver.get('http://www.baidu.com')
	driver.find_element_by_xpath('//*[@id="u1"]/a[5]').click()
	driver.find_element_by_xpath('//*[@id="wd1"]').send_keys('selenium')
	driver.find_element_by_css_selector('#tb_header_search_form > span.search_btn_wrap.search_btn_enter_ba_wrap > a').click()
	
	# 关注数和帖子数
	name=driver.find_element_by_xpath('//*[@id="pagelet_forum/pagelet/forum_card_number"]/span').text
	print(name)


	# 第一页标题
	# tab_list=driver.find_elements_by_class_name('threadlist_title')
	# for tab in tab_list:
	# 	print(tab.text)


	driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
	time.sleep(3)
	#前五页标题
	# for x in range(2,5):
	# 	tab_list=driver.find_elements_by_class_name('threadlist_title')
	# 	for tab in tab_list:
	# 		print(tab.text)
	# 	index = str(x)
	# 	# driver.find_element_by_link_text(index).click()
	# 	driver.find_element_by_css_selector('#frs_list_pager a').click()
	# 	time.sleep(5)
	
create_web()