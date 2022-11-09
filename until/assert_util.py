# -*- coding:utf-8 -*-
# @Time: 2022/9/28 10:54
# @Author: 小杨同学
# @Email: 541667133@qq.com
# @File: assert_util.py
import json

# 美化打印字典格式数据
def ppd(dic):
    print(json.dumps(dic, indent=2, ensure_ascii=False))

""" 封装json格式断言方法 """
"""
    d1-预期结果，d2-实际返回结果
    递归d2字典是不是和d1模板字典所期望值
    d1中 键开头是 ！，那么 d1 ！= d2
    d1中 键开头是 * ，那么表示这个key不应该存在
    d1中 键开头是 ？，可选字段，有的话进行验证，没有的略过
    d1中 键开头是 @ ，那么检查长度是否正确
    d1中 键开头是 [] ，那么检查只是否在一个范围内，例如[1,2,3,4]
    d1中 值是None， 只检查是否有这个键
    d1中 值不是None， 检查两个值是否一模一样
"""
def iterdict_dic(d1, d2):
    # 判断数据类型是否一样
    if type(d1) != type(d2):
        return False, f"数据类型不同 {d1}={type(d1)},{d2}={type(d2)}"
    # 判断字典内key和values是否期望值
    for k, v in d1.items():
        opposite = False  # 取反操作符
        if k[0] == '*':  # 如果键的开头是*，那么表示键在实际值中不应该存在
            k = k[1:]  # 取键的实际值
            if k in d2:
                return False, f'多余字段：{k}'
        elif k[0] == '@':  # 如果键的开头是@，那么values的长度和实际值应相等
            k = k[1:]
            if k not in d2:
                return False, f'缺少字段：{k}'
            if len(v) != len(d2[k]):
                return False, f'[{k}]的长度是：{len(v)}，实际长度：{len(d2[k])}'
        elif k[:2] == '[]':  # 如果键的开头是[]，那么实际值需要在预期值得范围内，比如实际值是1，预期值是[1,2,3]那么返回True
            k = k[2:]
            if k not in d2:
                return False, f'缺少字段：{k}'
            if d2[k] not in v:
                return False, f"[{k}]的值是:{d2[k]},不在期望值内[{v}]"
        elif k[0] == "?":
            k = k[1:]
            if k not in d2:
                continue
        elif k[0] == "!":
            k = k[1:]
            opposite = True

        if k not in d2:
            return False, f"缺少必要字段:[{k}]"
        if v == None:
            continue  # 如果values等于None，跳过
    if isinstance(v, dict):
        res, msg = iterdict_(v, d2[k])
        if res == False:
            return res, msg
    elif isinstance(v, list):
        if not isinstance(d2[k], list):
            return False, f"[{d2[k]}]是：{type(d2[k])},不是一个数组"
        if len(v) > len(d2[k]):
            return False, f"[{v}]长度和实际值:{d2[k]}长度不同"
        for i in range(0, len(v)):
            ret, msg = iterdict_(v[i], d2[k][i])
            if ret == False:
                return ret, msg
    elif opposite:
        if v == d2[k]:
            return False, f"[{k}]的值不应该等于[{v}]"
    else:
        if v != d2[k]:
            return False, f"[{k}]的期望值:[{v}] != 实际值:[{d2[k]}]:"


    return True, ""


def iterdict_(d1, d2):
    if type(d1) != type(d2):
        return False, f"数据类型不同 {d1}={type(d1)},{d2}={type(d2)}"

    # isinstance-主要用来判断变量是否属于某个内建类型，对象的类型与参数二的类型相同则返回True，否则返回False
    if isinstance(d1, dict):  # 如果预期值是字典格式则返回上面封装好的方法做判断
        return iterdict_dic(d1, d2)
    elif isinstance(d1, list):  # 如果预期值是列表格式则走下面方法
        if len(d1) > len(d2):
            return False, "列表长度不相等"
        # 循环列表断言列表值
        for i in range(0, len(d1)):
            ret, msg = iterdict_(d1[i], d2[i])  # 判断预期值是否等于实际值
            if ret == False:
                return ret, msg
            return True, ""
    else:
        if d1 != d2:
            return False, "预期值-[{d1}] != 实际值-[{d2}]"  # 判断预期值是否等于实际值
        else:
            return True, ""
        # 最后调用断言方法
def iterdict(d1, d2):
    ret, msg = iterdict_(d1, d2)
    assert ret, msg


if __name__ == '__main__':
    d1={'status': 100, 'description': '密码不能为空'}
    d2={'status': 200, 'description': '密码不能为空1'}
    d3 = ['status',200, 'description','密码不能为空1']
    print(iterdict(d1=d1, d2=d3))
