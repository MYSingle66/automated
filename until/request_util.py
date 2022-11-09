# -*- coding:utf-8 -*-
# @Time: 2022/9/27 12:49
# @Author: 小杨同学
# @Email: 541667133@qq.com
# @File: request_util.py
import requests
from until.loggerController import log
import allure

class RequestUtil:
    sess = requests.session()

    @allure.step("请求参数")
    def send_all_request(self, method, url, data, headers, **kwargs):
        """
        :param method:请求方式
        :param url:请求地址
        :param data:请求数据
        :param headers:请求头
        :param kwargs:其他请求参数
        :return:
        """
        res = RequestUtil.sess.request(method, url, data, headers)
        log.warning("------------------测试开始------------------")
        dict1={'请求地址':url, '请求方式':method, '请求头': headers,'请求数据':data}
        for k,v in dict1.items():
            log.info("{}：{}".format(k,v))
        # log.info("请求地址：{}".format(url))
        # log.info("请求方式：{}".format(method))
        # log.info("请求头：{}".format(headers))
        # log.info("请求数据：{}".format(data))
        return res