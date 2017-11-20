from package_manage import *


def test(tabName: '标签名'):
    find_ele_by_selector_and_html('.bui-tab-item-text', tabName).click()
    try:
        validate_nav(tabName)
    except Exception as e:
        print('导航路径跳转出错')
        exit()

    try:
        names = ['name', 'description', 'start', 'end',
                 'cardCodeNum', 'value', 'cardCodePrefix']
        successVals = ['现金抵扣卡', '该卡价值100元', '2018-06-01',
                       '2018-06-05', '10', '128.85', 'AX']
        errorVals = [error_text(), [], error_date('yyyy-mm-dd', True), error_date('yyyy-mm-dd', True),
                     error_positive_int(), error_money(), error_text()]
        validate_reset(names, successVals)
        validate_input_form(names, successVals, errorVals)
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, '编辑')))
        browser.find_element_by_partial_link_text("编辑").click()
        validate_reset(names[:-1], successVals, True)
        validate_input_form(names[:-1], successVals, errorVals)
    except Exception as e:
        print('表单验证出错')
        exit()

    try:
        browser.find_element_by_partial_link_text("查看关联卡号").click()
        # 对话框在iframe之外....
        browser.switch_to_default_content()
        find_ele_by_selector_and_html(
            '.bui-stdmod-footer button', '确定').click()
        browser.switch_to_frame(
            browser.find_elements_by_css_selector('iframe').pop())
        # 导出关联卡号
        browser.find_element_by_partial_link_text("导出关联卡号").click()
        browser.find_element_by_partial_link_text("删除").click()
        find_ele_by_selector_and_html('.bui-message button', '确定').click()
    except Exception as e:
        print('列表操作出错')
        exit()


def entity_card():
    select_menu('会员', '现金卡')
    test('现金卡')
    test('积分卡')
    browser.switch_to_default_content()

if __name__ == '__main__':
    entity_card()
