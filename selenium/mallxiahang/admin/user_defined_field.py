from package_manage import *

def test():
	
	try:
		validate_nav('会员自定义信息')
	except Exception as e:
		print('导航路径跳转出错')
		exit()

	try:
		names = ['fieldName','sortValue']
		successVals = ['测试字段1','9']
		errorVals = [error_text(),error_positive_int()]
		validate_reset(names,successVals)
		browser.find_elements_by_name('statusCd').pop().click()
		browser.find_elements_by_name('isRequired').pop().click()
		validate_input_form(names,successVals,errorVals)
		browser.find_element_by_partial_link_text("编辑").click()
		validate_reset(names,successVals,True)
		browser.find_element_by_name('statusCd').click()
		browser.find_element_by_name('isRequired').click()
		validate_input_form(names,successVals,errorVals)
	except Exception as e:
		print('表单验证出错')
		exit()

	try:
		browser.find_element_by_partial_link_text("删除").click()
		find_ele_by_selector_and_html('.bui-message button','确定').click()
	except Exception as e:
		print('列表操作出错')
		exit()

def user_defined_field():
	select_menu('会员','自定义信息')
	test()
	browser.switch_to_default_content()

if __name__ == '__main__':
	user_defined_field()