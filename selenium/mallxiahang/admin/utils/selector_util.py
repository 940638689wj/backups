from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()  # 谷歌
# browser = webdriver.Firefox()#火狐
# browser = webdriver.Ie()#ie

# browser.maximize_window()#窗口最大化8
browser.implicitly_wait(5)  # 最长元素等待时间
browser.get('http://localhost:8080/admin/sa')  # 访问地址
# browser.get('http://xh.dayang1.cn/admin/sa')  # 访问地址
# browser.get('http://www.baidu.com')#访问地址
# browser.find_element_by_id('kw').send_keys('selenium')
# browser.find_element_by_id('su').click()


def find_ele_by_selector_and_html(selector: '选择器', htmlStr: '标签内容'):
    # 根据选择器和标签内容获取第一个标签
    for i in browser.find_elements_by_css_selector(selector):
        if htmlStr in i.text:
            return i


def select_menu(topTab: '顶部菜单名', leftTab: '左部菜单名'):
    # 选择菜单
    find_ele_by_selector_and_html('.nav-item-inner', topTab).click()
    browser.find_element_by_partial_link_text(leftTab).click()
    # 进入iframe
    browser.switch_to_frame(
        browser.find_elements_by_css_selector('iframe').pop())


def validate_nav(tabName):
    print(tabName)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#grid button')))
    find_ele_by_selector_and_html('button', '添加').click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, tabName)))
    browser.find_element_by_partial_link_text(tabName).click()
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#grid button')))
    find_ele_by_selector_and_html('button', '添加').click()


def validate_reset(names: '输入框的name', successVals: '正确表单数据', isEdit: '是否为编辑操作'=False):
    # 重置按钮测试
    if isEdit:
        for name in names:
            browser.find_element_by_name(name).clear()
        browser.find_element_by_css_selector('button[type="reset"]').click()
        browser.find_element_by_name(name).clear()
    else:
        for i, name in enumerate(names):
            browser.find_element_by_name(name).send_keys(successVals[i])
        browser.find_element_by_css_selector('button[type="reset"]').click()


def validate_input_form(names: '输入框的name', successVals: '正确表单数据',
                        errorVals: '错误表单数据'):
    # 表单验证，逐条验证错误数据
    subBut = browser.find_element_by_css_selector('button[type="submit"]')
    for i, name in enumerate(names):
        browser.find_element_by_name(name).send_keys(successVals[i])

    for i, name in enumerate(names):
        for errorVal in errorVals[i]:
            time.sleep(1)
            browser.find_element_by_name(name).clear()
            browser.find_element_by_name(name).send_keys(errorVal)
            subBut.click()
            try:
                subBut.click()
            except Exception as e:
                print('表单', name, '验证出错！出错测试变量：', errorVal)
                exit()

        browser.find_element_by_name(name).clear()
        browser.find_element_by_name(name).send_keys(successVals[i])
    subBut.click()
