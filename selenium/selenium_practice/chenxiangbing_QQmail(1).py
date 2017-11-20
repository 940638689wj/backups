from selenium import webdriver
import time

def QQ_mail(driver):
	driver.get('https://mail.qq.com/')
	
	ele_iframe = driver.find_element_by_css_selector('#login iframe')

	driver.switch_to_frame(ele_iframe)

	driver.find_element_by_css_selector('#switch #switcher_plogin').click()
	#登录
	driver.find_element_by_css_selector('#u').send_keys('3197556044')
	driver.find_element_by_css_selector('#p').send_keys('abcd1234')
	time.sleep(1)
	driver.find_element_by_css_selector('#login_button').click()
	time.sleep(5)
	#进入主框架
	ele_iframe2 = driver.find_element_by_css_selector('#mainFrame')
	# driver.switch_to_frame(ele_iframe2)
	
	# mailinfol = driver.find_elements_by_css_selector('#TodayInBox li.mailinfo1.t_left2 a')

	# for unread_folder in mailinfol:
	#    print(unread_folder.text)
	#写信
	driver.switch_to_default_content()
	driver.find_element_by_css_selector('#composebtn_td').click()
	driver.switch_to_frame(ele_iframe2)
	driver.switch_to_active_element().send_keys('940638689')
	driver.find_element_by_css_selector('#subject').send_keys('这是一封辣鸡邮件')
	#信内容
	ele_iframe3 = driver.find_element_by_css_selector('#QMEditorArea table tbody tr:nth-child(2) td iframe')
	driver.switch_to_frame(ele_iframe3)
	driver.find_element_by_css_selector('body').click()
	driver.switch_to_active_element().send_keys('吃不吃鸡，嗨不嗨皮？')
	driver.switch_to_default_content()
	driver.switch_to_frame(ele_iframe2)
	driver.find_element_by_link_text('发送').click()









if __name__ == '__main__':
	driver = webdriver.Chrome()
	QQ_mail(driver)
