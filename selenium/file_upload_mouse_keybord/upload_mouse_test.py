from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
# driver.get('http://localhost:8081/admin/sa/productManage/addOrEdit')
driver.get('http://www.baidu.com')

# context_click() 右击
# double_click() 双击
# drag_and_drop() 拖动
# move_to_element() 鼠标悬停在一个元素上
# click_and_hold() 按下鼠标左键在一个元素上
ActionChains(driver).move_to_element(driver.find_element_by_link_text('设置')).perform()

# driver.find_element_by_id('kw').send_keys('aa')
# driver.find_element_by_id('kw').send_keys(Keys.LEFT)
# driver.find_element_by_id('kw').send_keys('bb')

# driver.find_element_by_css_selector('#form .soutu-btn').click()
# driver.find_element_by_css_selector('#form > div > div.soutu-state-normal > div.upload-wrap > input').send_keys('C:\\Users\\Administrator\\Desktop\\img\\sky.jpg')