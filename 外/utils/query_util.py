def select_chose(select_obj, option_obj):
    select_obj.click()
    option_obj.click()
    select_obj.click()


def move_to(browser):
    ele = browser.find_element_by_id('btnQuery')
    ActionChains(browser).move_to_element(ele).perform()


def query(browser, search_box_id, search_btn_id, input_params, select_params):
    browser.find_element_by_id(search_box_id).click()
    move_to()
    browser.find_element_by_id(search_btn_id).click()

    for input_param in input_params:
        browser.find_element_by_id(search_box_id).click()
        browser.find_element_by_id(input_param[0]).send_keys(input_param[1])
        move_to(browser)
        browser.find_element_by_id(search_btn_id).click()
        browser.find_element_by_id(input_param[0]).clear()
