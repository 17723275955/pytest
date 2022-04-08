#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2022-04-09 00:25:21
# @Author : 余少琪


import allure
import pytest
from config.setting import ConfigHandler
from utils.readFilesUtils.get_yaml_data_analysis import CaseData
from utils.assertUtils.assertControl import Assert
from utils.requestsUtils.requestControl import RequestControl


TestData = CaseData(ConfigHandler.data_path + r'Collect/collect_update_tool.yaml').case_process()


@allure.epic("开发平台接口")
@allure.feature("收藏模块")
class TestCollectUpdateTool:

    @allure.story("编辑收藏网址接口")
    @pytest.mark.parametrize('in_data', TestData, ids=[i['detail'] for i in TestData])
    def test_collect_update_tool(self, in_data, case_skip):
        """
        :param :
        :return:
        """

        res = RequestControl().http_request(in_data)
        Assert(in_data['assert']).assert_equality(response_data=res[0], sql_data=res[1])


if __name__ == '__main__':
    pytest.main(['test_collect_update_tool.py', '-s', '-W', 'ignore:Module already imported:pytest.PytestWarning'])
