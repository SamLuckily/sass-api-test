# -*- coding: utf-8 -*-
import allure
import pytest

from api.BaseApi import BaseApi
from api.UserManageApi import UserManageApi
from testcases.conftest import get_data


@allure.feature("用户管理模块")
class TestUserManageApi(BaseApi):
    def setup_class(self):
        self.user_manage = UserManageApi()

    @allure.story("获取用户列表测试用例")
    @allure.title("获取用户列表")
    @allure.severity('normal')
    @allure.description("获取用户列表")
    @pytest.mark.parametrize("data", get_data()['get_user_list'])
    def test_get_user_list(self, data):
        self.user_manage.get_user_list(data["page"], data["size"])
