import random
import string
'''
字符串辅助类
提供多种表单错误数据模板
'''


def get_length_str(length: '字符串长度'):
    # 获取指定长度的随机字符串
    str = ''
    for i in range(length):
        str += random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()')
    return str


def error_text():
    # 获取错误的文本模板
    return [get_length_str(300)]


def error_date(date_format: '日期格式', is_after_today: '是否要求大于今天'=False):
    # 获取错误的日期模板
    error_date_list = ['123', 'abc']
    if date_format.lower() == 'yyyy-mm-dd':
        error_date_list.append('2017-01')
    if date_format.lower() == 'yyyy-mm':
        error_date_list.append('2017-01-01')
    if is_after_today:
        error_date_list.append('1900-01-01')
    return error_date_list


def error_positive_int(is_include_zero: '是否允许等于0'=False):
    # 获取错误的正整数模板
    error_positive_int_list = ['abc', '-1', '2.34', '1234567890123456789']
    if not is_include_zero:
        error_positive_int_list.append('0')
    return error_positive_int_list


def error_money(is_include_zero: '是否允许等于0'=False):
    error_money_list = ['abc', '-1', '1234567890123456789']
    if not is_include_zero:
        error_money_list.append('0')
    return error_money_list
