# -*- coding: utf-8 -*-
import allure
import pytest
from api.AddressManageApi import AddressManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("地址管理模块")
class TestAddressManageApi:

    def setup_class(self):
        self.addr_manage = AddressManageApi()

    @allure.story("地址列表测试用例")
    @allure.title("地址列表")
    @allure.severity("normal")
    @allure.description("地址列表")
    def test_address_list(self):
        r = self.addr_manage.address_list()
        assert r.get("code") == 0

    @allure.story("添加地址测试用例")
    @allure.title("添加地址")
    @allure.severity("normal")
    @allure.description("添加地址")
    @pytest.mark.parametrize("data", get_data()["add_address"])
    def test_add_address(self, data):
        # 添加地址
        r = self.addr_manage.add_address(data["title"])
        assert r.get("code") == 0
        uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 删除地址
        r = self.addr_manage.del_address(uuid)
        assert r.get("code") == 0

    @allure.story("编辑地址测试用例")
    @allure.title("编辑地址")
    @allure.severity("normal")
    @allure.description("编辑地址")
    @pytest.mark.parametrize("data", get_data()["edit_address"])
    def test_edit_address(self, data):
        # 添加地址
        r = self.addr_manage.add_address(data["title"])
        assert r.get("code") == 0
        uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 编辑地址
        r = self.addr_manage.edit_address(data["titles"], uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(uuid)
        assert r.get("code") == 0

    @allure.story("地址移动测试用例")
    @allure.title("地址移动")
    @allure.severity("normal")
    @allure.description("地址移动")
    @pytest.mark.parametrize("data", get_data()["address_relocation"])
    def test_address_relocation(self, data):
        # 添加地址
        r = self.addr_manage.add_address(data["title_one"])
        uuid_one = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        r = self.addr_manage.add_address(data["title_two"])
        uuid_two = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        # 移动地址
        r = self.addr_manage.address_relocation(uuid_one, uuid_two, data["rel"], data["loc"])
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(uuid_one)
        assert r.get("code") == 0
        r = self.addr_manage.del_address(uuid_two)
        assert r.get("code") == 0
