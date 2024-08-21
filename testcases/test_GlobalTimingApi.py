# -*- coding: utf-8 -*-
import allure
import pytest

from api.GlobalTimingApi import GlobalTimingApi
from testcases.conftest import get_data


@allure.feature("全局定时模块")
class TestGlobalTimingApi:

    def setup_class(self):
        self.global_time = GlobalTimingApi()

    @allure.story("编辑定时任务测试用例")
    @allure.title("编辑定时任务")
    @allure.severity("normal")
    @allure.description("编辑定时任务")
    @pytest.mark.parametrize("data", get_data()["edit_time_task"])
    def test_edit_time_task(self, data):
        r = self.global_time.edit_time_task(data["is_global_timing"], data["on_type"], data["on_status"],
                                            data["on_device"],
                                            data["on_timer"], data["lession_on_timer"], data["on_week"],
                                            data["off_status"],
                                            data["off_device"], data["off_timer"], data["off_week"])
        assert r.get("code") == 0
        r = self.global_time.edit_time_task(data["not_global_timing"], data["on_type"], data["on_status"],
                                            data["on_device"],
                                            data["on_timer"], data["lession_on_timer"], data["on_week"],
                                            data["off_status"],
                                            data["off_device"], data["off_timer"], data["off_week"])
        assert r.get("code") == 0

    @allure.story("获取定时任务信息测试用例")
    @allure.title("获取定时任务信息")
    @allure.severity("normal")
    @allure.description("获取定时任务信息")
    def test_get_time_task(self):
        r = self.global_time.get_time_task()
        assert r.get("code") == 0
