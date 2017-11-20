from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import random

# from utils.start_util import *
# num=0
# num=1
num=2

driver = webdriver.Chrome()
# driver.maximize_window()
code_list = ['18950169610&&2&&4199600962ecb914d46a60d111beca5d444d9a70',
'15860632899&&2&&fddcb60c6001eb3beaaac33d68890ac46eec8f0e',
'18965826939&&2&&7369ae8d74de079b9d403c0156193dbbc445e64a']
driver.get('http://lbdct.dayang1.cn/admin/sa/main#ordercheck/setting:role')
driver.delete_cookie('JSESSIONID')
cookie_list = ['E15A3F170F0A5EEDB8318A1EF5016A62',
'C66E7E87FEFC784E3C987BA7CFD24F1A',
'54F7D33D74F0967DC79DC7E6748528F2']

driver.add_cookie({'name': 'JSESSIONID', 'value': cookie_list[num]})
driver.get('http://lbdct.dayang1.cn/admin/sa/main#ordercheck/setting:role')
time.sleep(1)

driver.switch_to_frame(driver.find_element_by_tag_name('iframe'))
for x in range(1,300):
	time.sleep(random.uniform(1, 2))
	driver.find_element_by_id('orderNumber').send_keys(code_list[num])
	time.sleep(0.5)
	driver.find_element_by_id('btnSearch').click()
	driver.find_element_by_id('orderNumber').clear()
	time.sleep(0.5)
	# info = driver.find_element_by_css_selector('#showMesg li')
	# print(info.find_element_by_css_selector('span').text 
	# 	+ info.find_element_by_css_selector('.orderinfo').text
	# 	+ info.find_elements_by_css_selector('p em')[-1].text)
