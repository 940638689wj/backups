from chenxiangbin import creat_order
from chenxiangbin2 import creat_goods
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
creat_order(driver)
creat_goods(driver)