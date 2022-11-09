# -*- coding:utf-8 -*-
# @Time: 2022/9/28 12:29
# @Author: 小杨同学
# @Email: 541667133@qq.com
# @File: assert_utils.py
# -*- coding: utf-8 -*-
# @Time : 2021/12/13 14:07
# @Author : Limusen
# @File : check_utils
import operator
from until.loggerController import log
import allure
@allure.step("预期结果-返回结果")
def validate(expected_result,actual_result):
    """
    :param expected_result: 预期结果
    :param actual_result: 实际返回结果
    :return:
    """
    # 判断数据类型是否相同
    if type(expected_result) != type(actual_result):
        log.debug(f"数据类型不同 {expected_result}={type(expected_result)},{actual_result}={type(actual_result)}")
        log.warning("------------------测试结束------------------")
        return False, f"数据类型不同 {expected_result}={type(expected_result)},{actual_result}={type(actual_result)}"
    #判断两个字典键值对个数是否一样
    # print(expected_result)
    # print(len(expected_result))
    if len(expected_result)>len(actual_result):
        keys = set(expected_result) - set(actual_result)
        for i in list(keys):
            log.warning(f"缺少字段：{i}")
            log.info("------------------测试结束------------------")
            return False, f'缺少字段：{i}'
    elif len(expected_result)<len(actual_result):
        keys = set(actual_result) - set(expected_result)
        for i in list(keys):
            log.debug(f"多余字段：{i}")
            log.warning("------------------测试结束------------------")
            return False, f'多余字段：{i}'
    for k,v in expected_result.items():
        # print(k,v)
    #     if v == actual_result[k]:
    #         return False, f"[{k}]的值不应该等于[{v}]"
    # else:
        if v != actual_result[k]:
            log.debug(f"[{k}]的期望值:[{v}] != 实际值:[{actual_result[k]}]:")
            log.warning("------------------测试结束------------------")
            return False, f"[{k}]的期望值:[{v}] != 实际值:[{actual_result[k]}]:"
    # if expected_result != actual_result:
    #     keys = set(actual_result) - set(expected_result)
    #     return False, f'多余字段：{keys}'
    # 判断字典内key和values是否期望值
    if operator.eq(expected_result, actual_result) == True:
        log.debug("没有问题了，断言通过，下班")
        log.warning("------------------测试结束------------------")
        return True, f"断言通过"


def iterdict_(expected_result, actual_result):
    if type(expected_result) != type(actual_result):
        log.debug(f"数据类型不同 {expected_result}={type(expected_result)},{actual_result}={type(actual_result)}")
        return False, f"数据类型不同 {expected_result}={type(expected_result)},{actual_result}={type(actual_result)}"

    # isinstance-主要用来判断变量是否属于某个内建类型，对象的类型与参数二的类型相同则返回True，否则返回False
    if isinstance(expected_result, dict):  # 如果预期值是字典格式则返回上面封装好的方法做判断
        return validate(expected_result, actual_result)
    elif isinstance(expected_result, list):  # 如果预期值是列表格式则走下面方法
        if len(expected_result) > len(actual_result):
            return False, "列表长度不相等"
        # 循环列表断言列表值
        for i in range(0, len(expected_result)):
            ret, msg = iterdict_(expected_result[i], actual_result[i])  # 判断预期值是否等于实际值
            if ret == False:
                return ret, msg
            return True, ""
    else:
        if expected_result != actual_result:
            return False, "预期值-[{d1}] != 实际值-[{d2}]"  # 判断预期值是否等于实际值
        else:
            return True, ""
        # 最后调用断言方法
def iterdicts(expected_result, actual_result):
    ret, msg = iterdict_(expected_result, actual_result)
    assert ret, msg

if __name__ == '__main__':
    theString = 'Hello Hamcrest'
    myString = 'Hello Hamcrest'
    a = {'status': 100, 'description': '密码不能为空'}
    b = {'status': 100, 'description': '密码不能为空', "age": 20}
    c = {'status': 100}
    d = {'status': 100, 'description': '密码不能为空'}
    # print(validate(d1, d2))
    # keys = set(b) - set(a)
    # value = {k: b[k] for k in set(b) - set(a)}
    # print(keys)
    # print(value)
    # print(iterdicts(a, b))
    # print(iterdicts(a, c))
    print("---------------------------")
    print(iterdicts(a,d))