from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('http://posxs.dayang1.cn/admin/pc/login')

# 对于下拉框（Select标签）需要单独的处理方式
org_select = driver.find_element_by_id('orgId')
time.sleep(2)
Select(org_select).select_by_value('7')