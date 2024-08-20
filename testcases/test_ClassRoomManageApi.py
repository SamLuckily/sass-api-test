# -*- coding: utf-8 -*-
import allure
import pytest

from api.AddressManageApi import AddressManageApi
from api.ClassRoomManageApi import ClassRoomManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils
from utils.time_stamp_utils import TimeStampUtils


@allure.feature("教室管理模块")
class TestChatRoomManageApi:

    def setup_class(self):
        self.classroom_manage = ClassRoomManageApi()
        self.addr_manage = AddressManageApi()

    @allure.story("空闲主讲教室列表测试用例")
    @allure.title("空闲主讲教室列表")
    @allure.severity("normal")
    @allure.description("空闲主讲教室列表")
    @pytest.mark.parametrize("data", get_data()["idle_speaker"])
    def test_idle_speaker(self, data):
        start_time = TimeStampUtils.get_current_timestamp()[0]
        end_time = TimeStampUtils.get_current_timestamp()[1]
        r = self.classroom_manage.idle_speaker(start_time, end_time, data["live_mode"], data["room_type"])
        assert r.get("code") == 0

    @allure.story("空闲听课教室列表测试用例")
    @allure.title("空闲听课教室列表")
    @allure.severity("normal")
    @allure.description("空闲听课教室列表")
    @pytest.mark.parametrize("data", get_data()["idle_listener"])
    def test_idle_listener(self, data):
        start_time = TimeStampUtils.get_current_timestamp()[0]
        end_time = TimeStampUtils.get_current_timestamp()[1]
        r = self.classroom_manage.idle_speaker(start_time, end_time, data["live_mode"], data["room_type"])
        room_id = JsonPathUtils.get(r, "$..list[(@.length-1)].id")
        assert r.get("code") == 0
        r = self.classroom_manage.idle_listener(start_time, end_time, room_id, data["room_type"])
        assert r.get("code") == 0

    @allure.story("添加教室测试用例")
    @allure.title("添加教室")
    @allure.severity("normal")
    @allure.description("添加教室")
    @pytest.mark.parametrize("data", get_data()["add_classroom"])
    def test_add_classroom(self, data):
        # 添加地址
        r = self.addr_manage.add_address(data["address"])
        addr_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        # 添加教室
        r = self.classroom_manage.add_classroom(data["title"], addr_uuid)
        assert r.get("code") == 0
        # 获取教室列表
        r = self.classroom_manage.classroom_list(data["page"], data["size"], data["status"], addr_uuid)
        classroom_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("编辑教室测试用例")
    @allure.title("编辑教室")
    @allure.severity("normal")
    @allure.description("编辑教室")
    @pytest.mark.parametrize("data", get_data()["edit_classroom"])
    def test_edit_classroom(self, data):
        # 添加地址
        r = self.addr_manage.add_address(data["address"])
        addr_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        # 添加教室
        r = self.classroom_manage.add_classroom(data["title"], addr_uuid)
        assert r.get("code") == 0
        # 获取教室列表
        r = self.classroom_manage.classroom_list(data["page"], data["size"], data["status"], addr_uuid)
        classroom_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 编辑教室
        self.classroom_manage.edit_classroom(classroom_uuid, data["edit_title"])
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("教室状态统计测试用例")
    @allure.title("教室状态统计")
    @allure.severity("normal")
    @allure.description("教室状态统计")
    def test_classroom_status(self):
        r = self.classroom_manage.classroom_status()
        assert r.get("code") == 0

    @allure.story("教室列表（带设备状态）测试用例")
    @allure.title("教室列表（带设备状态）")
    @allure.severity("normal")
    @allure.description("教室列表（带设备状态）")
    @pytest.mark.parametrize("data", get_data()["classroom_list"])
    def test_classroom_list(self, data):
        # 添加地址
        r = self.addr_manage.add_address(data["address"])
        addr_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        # 添加教室
        r = self.classroom_manage.add_classroom(data["title"], addr_uuid)
        assert r.get("code") == 0
        # 获取教室列表
        r = self.classroom_manage.classroom_list(data["page"], data["size"], data["status"], addr_uuid)
        classroom_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("教室列表(下拉框展示)测试用例")
    @allure.title("教室列表(下拉框展示)")
    @allure.severity("normal")
    @allure.description("教室列表(下拉框展示)")
    @pytest.mark.parametrize("data", get_data()["classroom_list_select"])
    def test_classroom_list_select(self, data):
        r = self.classroom_manage.classroom_list_select(data["page"], data["size"])
        assert r.get("code") == 0

    @allure.story("教室详情测试用例")
    @allure.title("教室详情")
    @allure.severity("normal")
    @allure.description("教室详情")
    @pytest.mark.parametrize("data", get_data()["classroom_detail"])
    def test_classroom_detail(self, data):
        # 添加地址
        r = self.addr_manage.add_address(data["address"])
        addr_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        # 添加教室
        r = self.classroom_manage.add_classroom(data["title"], addr_uuid)
        assert r.get("code") == 0
        # 获取教室列表
        r = self.classroom_manage.classroom_list(data["page"], data["size"], data["status"], addr_uuid)
        classroom_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        assert r.get("code") == 0
        # 获取教室详情
        r = self.classroom_manage.classroom_detail(classroom_uuid)
        assert r.get("code") == 0
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0
