from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.find_element_by_css_selector('#form .soutu-btn').click()
# driver.find_element_by_css_selector('#form .upload-pic').send_keys('C:\\Users\\Administrator\\Desktop\\img\\sky.jpg')

# driver.find_element_by_id('kw').send_keys('aa')
# driver.find_element_by_id('kw').send_keys(Keys.LEFT)
# driver.find_element_by_id('kw').send_keys('bb')
# ele = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(ele).perform()
ele = driver.find_element_by_id('su')
ActionChains(driver).context_click(ele).send_keys(Keys.DOWN).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()

