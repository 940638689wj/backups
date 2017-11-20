from selenium import webdriver

browser = webdriver.Chrome()#火狐
browser.maximize_window()#窗口最大化
browser.implicitly_wait(10)#最长元素等待时间
browser.get('http://15181ca208.imwork.net/ebihm/login')#访问地址


def find_ele_by_selector_and_html(selector:'选择器',htmlStr:'标签内容'):
	#根据选择器和标签内容获取第一个标签
	for i in browser.find_elements_by_css_selector(selector):
		if htmlStr in i.text:
			return i
			
def select_tabs(tabs_name:'标签名数组'):
	for tab_name in tabs_name[:-1]:
		ele = browser.find_element_by_partial_link_text(tab_name)
		ActionChains(browser).move_to_element(ele).perform()
	WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,tabs_name[-1])))
	browser.find_element_by_partial_link_text(tabs_name[-1]).click()
	browser.switch_to_frame(browser.find_elements_by_css_selector('iframe').pop())	

def validate_reset(names:'输入框的name',successVals:'正确表单数据',isEdit:'是否为编辑操作'=False):
	#重置按钮测试
	if isEdit:
		for name in names:
			browser.find_element_by_name(name).clear()
		browser.find_element_by_css_selector('button[type="reset"]').click()
		browser.find_element_by_name(name).clear()
	else:
		for i,name in enumerate(names):
			browser.find_element_by_name(name).send_keys(successVals[i])
		browser.find_element_by_css_selector('button[type="reset"]').click()

def validate_input_form(names:'输入框的name',successVals:'正确表单数据',
	errorVals:'错误表单数据'):
	# 表单验证，逐条验证错误数据
	subBut = browser.find_element_by_css_selector('#btnCardSave')
	for i,name in enumerate(names):
		browser.find_element_by_name(name).send_keys(successVals[i])

	for i,name in enumerate(names):
		for errorVal in errorVals[i]:
			browser.find_element_by_name(name).clear()
			browser.find_element_by_name(name).send_keys(errorVal)
			subBut.click()
			try:
				subBut.click()
			except Exception as e: 
				print('表单',name,'验证出错！出错测试变量：',errorVal)
				exit()
			
		browser.find_element_by_name(name).clear()
		browser.find_element_by_name(name).send_keys(successVals[i])
	subBut.click()

def login_form(name:'账号',password:'密码'):
	browser.find_element_by_id('loginName').send_keys(name)
	browser.find_element_by_id('loginPassword').send_keys(password)
	browser.find_element_by_id('btnLogin').click()

