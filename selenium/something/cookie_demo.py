from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('http://xh.dayang1.cn/account/order?orderTypeCd=1')

driver.delete_cookie('JSESSIONID')
driver.add_cookie({"name":"JSESSIONID", "value":"2DD8484ACFA1EAC4ED71F9091C6ADFEF"})
driver.refresh()
