# -*- coding: utf-8 -*-
import allure
import pytest

from api.ProfileApi import ProfileApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("情景模式模块")
class TestProfileApi:

    def setup_class(self):
        self.profile = ProfileApi()

    @allure.story("获取情景模式列表测试用例")
    @allure.title("获取情景模式列表")
    @allure.severity("normal")
    @allure.description("获取情景模式列表")
    def test_profile(self):
        self.profile.profile()

    @allure.story("添加情景模式测试用例")
    @allure.title("添加情景模式")
    @allure.severity("normal")
    @allure.description("添加情景模式")
    @pytest.mark.parametrize("data", get_data()['add_profile'])
    def test_add_profile(self, data):
        setting = [
            {
                "port": 1,
                "value": 0
            },
            {
                "port": 2,
                "value": 0
            },
            {
                "port": 3,
                "value": 0
            },
            {
                "port": 4,
                "value": 0
            }
        ]
        r = self.profile.add_profile(data["title"], setting)
        assert r.get("code") == 0
        r = self.profile.profile()
        uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        r = self.profile.del_profile(uuid)
        assert r.get("code") == 0

    @allure.story("编辑情景模式测试用例")
    @allure.title("编辑情景模式")
    @allure.severity("normal")
    @allure.description("编辑情景模式")
    @pytest.mark.parametrize("data", get_data()['edit_profile'])
    def test_edit_profile(self, data):
        # 添加情景模式
        setting = [
            {
                "port": 1,
                "value": 0
            },
            {
                "port": 2,
                "value": 0
            },
            {
                "port": 3,
                "value": 0
            },
            {
                "port": 4,
                "value": 0
            }
        ]
        r = self.profile.add_profile(data["title"], setting)
        assert r.get("code") == 0
        # 获取情景模式列表
        r = self.profile.profile()
        uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 编辑情景模式
        r = self.profile.edit_profile(uuid, data["edit_title"], setting)
        assert r.get("code") == 0
        # 删除情景模式
        r = self.profile.del_profile(uuid)
        assert r.get("code") == 0
