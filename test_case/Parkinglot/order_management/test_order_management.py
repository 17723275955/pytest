#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2023-04-20 14:13:41


import allure
import pytest
from utils.read_files_tools.get_yaml_data_analysis import GetTestCase
from utils.assertion.assert_control import Assert
from utils.requests_tool.request_control import RequestControl
from utils.read_files_tools.regular_control import regular
from utils.requests_tool.teardown_control import TearDownHandler


case_id = ['no_compleorder_search1', 'no_compleorder_detail1', 'no_compleorder_plate_correct1', 'no_compleorder_plate_exception1', 'compleorder_search1', 'compleorder_detail1']
TestData = GetTestCase.case_data(case_id)
re_data = regular(str(TestData))


@allure.epic("停车接口")
@allure.feature("订单管理模块")
class TestOrderManagement:

    @allure.story("订单信息")
    @pytest.mark.parametrize('in_data', eval(re_data), ids=[i['detail'] for i in TestData])
    def test_order_management(self, in_data, case_skip):
        """
        :param :
        :return:
        """
        res = RequestControl(in_data).http_request()
        TearDownHandler(res).teardown_handle()
        Assert(in_data['assert_data']).assert_equality(response_data=res.response_data,
                                                       sql_data=res.sql_data, status_code=res.status_code)


if __name__ == '__main__':
    pytest.main(['test_order_management.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
