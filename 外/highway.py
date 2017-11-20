from package_manage import *


def test(tabs_name: '标签名数组'):
    select_tabs(tabs_name)

    browser.find_element_by_id('btnSearch').click()

    browser.find_element_by_id('searchbox').click()
    move_to()
    browser.find_element_by_id('btnQuery').click()

    browser.find_element_by_id('searchbox').click()
    browser.find_element_by_name('routeCode').send_keys('123')
    move_to()
    browser.find_element_by_id('btnQuery').click()

    browser.find_element_by_id('searchbox').click()
    browser.find_element_by_name('routeCode').clear()
    browser.find_element_by_name('routeName').send_keys('123')
    move_to()
    browser.find_element_by_id('btnQuery').click()

    browser.find_element_by_id('searchbox').click()
    browser.find_element_by_name('routeName').clear()

    for opt in browser.find_elements_by_css_selector('#hl option'):
        browser.find_element_by_id('searchbox').click()
        select_chose(browser.find_element_by_name('highwayLevelCode'), opt)
        move_to()
        browser.find_element_by_id('btnQuery').click()

    browser.find_element_by_id('btnAdd').click()

    select_chose(browser.find_element_by_id('highwayLevelCode'),
                 browser.find_elements_by_css_selector('#highwayLevelCode option')[1])
    select_chose(browser.find_element_by_id('administrativeLevelCode'),
                 browser.find_elements_by_css_selector('#administrativeLevelCode option')[1])
    select_chose(browser.find_element_by_id('routeDirectionCode'),
                 browser.find_elements_by_css_selector('#routeDirectionCode option')[1])

    browser.find_element_by_id('startStake').send_keys('1')
    browser.find_element_by_id('endStake').send_keys('2')
    time.sleep(2)
    for addbtn in browser.find_elements_by_css_selector('.datagrid-toolbar'):
        ele = addbtn.find_element_by_partial_link_text('增行')
        ActionChains(browser).move_to_element(ele).perform()
        ele.click()

    names = ['routeCode', 'routeName', 'startStake', 'endStake', 'startPosition', 'endPosition',
             'openingTime', 'remark']
    successVals = ['测试路线编码3', '测试路线名称3', '5', '20', '测试起点位置3', '测试终点位置3',
                   '2017-08', '测试备注：这里是备注这里是备注这里是备注3']
    # errorVals = [getErrorText(),getErrorText(),getErrorInt(),getErrorInt(),getErrorText(),getErrorText(),
    # 	['abc','123','2017-'],getErrorText()]

    errorVals = [[], [], [], [], [], [],
                 [], []]

    validate_input_form(names, successVals, errorVals)

    time.sleep(2)
    browser.find_element_by_id('btnCardBack').click()

    browser.find_element_by_id('searchbox').click()
    select_chose(browser.find_element_by_id('hl'),
                 browser.find_elements_by_css_selector('#hl option')[1])
    browser.find_element_by_id('btnQuery').click()

    time.sleep(2)
    browser.find_element_by_class_name(
        'datagrid-btable').find_elements_by_name('CheckId').pop().click()
    browser.find_element_by_partial_link_text('删除').click()
    findBySelectorAndHtml('.l-btn-text', '确定').click()

    browser.find_element_by_class_name(
        'datagrid-btable').find_elements_by_name('CheckId').pop().click()

    browser.find_element_by_partial_link_text('导出').click()


login_form('liuxy1', '123456')
test(['基础数据', '路线'])
