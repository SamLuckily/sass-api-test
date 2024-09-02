# -*- coding: utf-8 -*-
import allure
import pytest

from api.EquipmentManageApi import EquipmentManageApi
from testcases.conftest import get_data


class TestEquipmentManageApi:

    def setup_class(self):
        self.equipment_manage = EquipmentManageApi()

    @allure.story("设备列表测试用例")
    @allure.title("设备列表")
    @allure.severity("normal")
    @allure.description("设备列表")
    @pytest.mark.parametrize("data", get_data()["equipment_manage"])
    def test_equipment_list(self, data):
        r = self.equipment_manage.equipment_list(data["page"], data["size"])
        assert r.get("code") == 0

    @allure.story("设备列表(下拉框展示)测试用例")
    @allure.title("设备列表(下拉框展示)")
    @allure.severity("normal")
    @allure.description("设备列表(下拉框展示)")
    @pytest.mark.parametrize("data", get_data()["equipment_manage"])
    def test_equipment_list_display(self, data):
        r = self.equipment_manage.equipment_list_display(data["page"], data["size"])
        assert r.get("code") == 0
