# -*- coding:utf-8 -*-
# @Time: 2022/9/27 18:20
# @Author: 小杨同学
# @Email: 541667133@qq.com
# @File: read_data.py
def read_all_data(caseinfo):
    names = caseinfo["dcaseid"]
    methods = caseinfo["dmethod"]
    urls = caseinfo["durl"]
    headers = caseinfo["dheaders"]
    datas = caseinfo["ddate"]
    validates = caseinfo["dexcepted_res"]
    list1 = [names, methods, urls, headers, datas, validates]
    return list1

if __name__ == '__main__':
    caseinfo={
        "dcaseid": "test_case_001登录成功",
        "ddate": {
            "keywords": 17026958246,
            "password": "aa123456"
        },
        "dexcepted_res": {
            "description": "登录成功",
            "status": 200
        },
        "dheaders": {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        "dmethod": "post",
        "durl": "http://user-p2p-test.itheima.net/member/public/login"
    }
    print(read_all_data(caseinfo))