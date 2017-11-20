from package_manage import *


def test(tabName: '标签名'):
    find_ele_by_selector_and_html('.bui-tab-item-text', tabName).click()
    try:
        validate_nav(tabName)
    except Exception as e:
        print('导航路径跳转出错')
        exit()

    try:
        names = ['promotionName', 'groupcouponDesc', 'grouponInitSaleNum', 'grouponMaxSaleNum',
                 'grouponPersonQuotaNum', 'grouponPrice', 'enableStart', 'enableEnd', 'allowUseStart', 'allowUseEnd']
        successVals = ['测试团购1', '测试团购描述111', '1000', '2000',
                       '5', '128.98', '2018-06-01', '2018-06-05', '2018-06-05', '2018-06-10']
        errorVals = [error_text(), [], error_positive_int(), error_date('yyyy-mm-dd', True), error_date('yyyy-mm-dd', True),
                     error_positive_int(), error_money(), error_text()]
        validate_reset(names, successVals)
        browser.find_elements_by_name('statusCd').pop().click()
        browser.find_elements_by_id('allUserLevel').click()
        browser.find_elements_by_id('allUserLevel').click()
        browser.find_elements_by_name('userLevel')[0].click()
        browser.find_elements_by_name('userLevel')[-1].click()

        validate_input_form(names, successVals, errorVals)
        browser.find_element_by_partial_link_text("编辑").click()
        validate_reset(names, successVals, True)
        browser.find_element_by_name('statusCd').click()
        validate_input_form(names, successVals, errorVals)
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


def promotion_groupon():
    select_menu('票券', '团购列表')
    test('可用团购')
    browser.switch_to_default_content()

promotion_groupon()
