import pytest
import os
import allure

from until.assert_util import iterdict
from until.assert_utils import validate, iterdicts
from until.excel_util import read_data_all
from until.handle_path import data_path
from until.read_data import read_all_data
from until.request_util import RequestUtil
from until.loggerController import log

@allure.epic('金融系统测试')
@allure.feature('登录模块测试')
class TestApi:

    @allure.severity('critical') # 用例等级
    @allure.story("登录用例")
    # @allure.title('登录接口测试用例')  # 测试用例标题
    @pytest.mark.parametrize("caseinfo",read_data_all(os.path.join(data_path,'apitest.xlsx'),'Sheet1'))
    def test_login_success(self,caseinfo):
        # print(caseinfo)
        data=read_all_data(caseinfo)
        res = RequestUtil().send_all_request(method=data[1],url=data[2],data=data[4],headers=data[3])
        # ReadData().assert_utils(data[6],data[7],res.json().get('status'),res.json().get('description'))
        allure.dynamic.title(data[0])


        log.info("预期结果：{}".format(data[5]))
        log.info("实际结果：{}".format(res.json()))
        # dy = iterdict(data[5],res.json())
        dy = iterdicts(data[5], res.json())
        # print(str(dy))
        # allure.attach(body=str(dy), attachment_type=allure.attachment_type.TEXT)
        # print(res.json())