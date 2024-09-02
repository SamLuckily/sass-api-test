# -*- coding: utf-8 -*-
import allure
from api.SystemManagementApi import SystemManagementApi


class TestSystemManagementApi:

    def setup_class(self):
        self.system_manage = SystemManagementApi()

    @allure.story("主页配置保存测试用例")
    @allure.title("主页配置保存")
    @allure.severity("normal")
    @allure.description("主页配置保存")
    def test_homepage_config_save(self):
        """"主页配置保存"""
        self.system_manage.homepage_config_save()
