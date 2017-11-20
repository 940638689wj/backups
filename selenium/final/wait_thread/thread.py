from selenium import webdriver
import time,threading

def select_text(select_str):
	driver = webdriver.Chrome()
	driver.get('http://www.baidu.com')
	driver.find_element_by_id('kw').clear()
	driver.find_element_by_id('kw').send_keys(select_str)
	driver.find_element_by_id("su").click()
	for x in range(1,2):
		time.sleep(3)
		driver.find_element_by_partial_link_text('下一页').click()



select_list = ['selenium', 'qtp', 'winner']

for select_str in select_list:
	# 开启线程
	# select_text(select_str)
	t = threading.Thread(target=select_text, args=[select_str])
	t.start()
	t.join()

