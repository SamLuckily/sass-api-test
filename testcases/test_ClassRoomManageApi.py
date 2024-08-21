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

    @allure.story("保存教室配置信息测试用例")
    @allure.title("保存教室配置信息")
    @allure.severity("normal")
    @allure.description("保存教室配置信息")
    @pytest.mark.parametrize("data", get_data()["save_classroom_config_info"])
    def test_save_classroom_config_info(self, data):
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
        # 保存教室配置信息接口入参
        base_conf = {
            "total_power": 0,
            "threshold": 250,
            "controller": "0",
            "video_width": 1920,
            "video_height": 1080,
            "min_code_rate": 4000,
            "max_code_rate": 6000,
            "frame_rate": 25,
            "classroom_ip": ""
        }
        cmd_conf = {
            "current_threshold": "200",
            "power_off_delay": "10",
            "power_off_max_delay": "120",
            "axbox_ip": "192.168.127.1",
            "axbox_port": "4001",
            "power_ip": "192.168.0.7",
            "power_port": "24",
            "oem_ip": "192.168.127.8",
            "oem_port": "24",
            "enable": "1",
            "device_ctrl_mode": "0",
            "curtain_ctrl_mode": "1",
            "lights": None,
            "airconds": None,
            "curtains": None,
            "lights_per_module": "6",
            "airconds_per_module": "1",
            "curtains_per_module": "1",
            "projector_open": "",
            "projector_close": "",
            "poweron_time_seq": [{
                "port": "0",
                "type": "1",
                "delay": "0"
            }, {
                "port": "1",
                "type": "1",
                "delay": "0"
            }, {
                "port": "2",
                "type": "1",
                "delay": "0"
            }, {
                "port": "3",
                "type": "3",
                "delay": "0"
            }, {
                "port": "4",
                "type": "1",
                "delay": "0"
            }, {
                "port": "5",
                "type": "1",
                "delay": "30"
            }, {
                "port": "6",
                "type": "1",
                "delay": "0"
            }, {
                "port": "7",
                "type": "1",
                "delay": "0"
            }],
            "poweroff_time_seq": [{
                "port": "0",
                "type": "1",
                "delay": "0"
            }, {
                "port": "1",
                "type": "1",
                "delay": "0"
            }, {
                "port": "2",
                "type": "1",
                "delay": "0"
            }, {
                "port": "3",
                "type": "3",
                "delay": "0"
            }, {
                "port": "4",
                "type": "1",
                "delay": "10"
            }, {
                "port": "5",
                "type": "1",
                "delay": "0"
            }, {
                "port": "6",
                "type": "1",
                "delay": "0"
            }, {
                "port": "7",
                "type": "1",
                "delay": "0"
            }]
        }
        share_conf = {
            "share_status": 0
        }
        r = self.classroom_manage.save_classroom_config_info(classroom_uuid, base_conf, cmd_conf, share_conf)
        assert r.get("code") == 0
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("获取教室配置信息测试用例")
    @allure.title("获取教室配置信息")
    @allure.severity("normal")
    @allure.description("获取教室配置信息")
    @pytest.mark.parametrize("data", get_data()["get_classroom_config_info"])
    def test_get_classroom_config_info(self, data):
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
        r = self.classroom_manage.get_classroom_config_info(classroom_uuid)
        assert r.get("code") == 0
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("教室添加设备测试用例")
    @allure.title("教室添加设备")
    @allure.severity("normal")
    @allure.description("教室添加设备")
    @pytest.mark.parametrize("data", get_data()["classroom_add_device"])
    def test_classroom_add_device(self, data):
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
        # 教室添加设备
        r = self.classroom_manage.classroom_add_device(classroom_uuid, data["line"], data["cport"], data["titles"])
        msg = JsonPathUtils.get(r, "$..msg")[0]
        assert msg == "没有查询到相关网关，无法添加设备"
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("获取教室设备类型以及限制数测试用例")
    @allure.title("获取教室设备类型以及限制数")
    @allure.severity("normal")
    @allure.description("获取教室设备类型以及限制数")
    @pytest.mark.parametrize("data", get_data()["classroom_device_type"])
    def test_classroom_device_type(self, data):
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
        # 获取教室设备类型以及限制数
        self.classroom_manage.classroom_device_type()
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("一键开关测试用例")
    @allure.title("一键开关")
    @allure.severity("normal")
    @allure.description("一键开关")
    @pytest.mark.parametrize("data", get_data()["one_key_switch"])
    def test_one_key_switch(self, data):
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
        # 一键开关
        r = self.classroom_manage.one_key_switch(data["status"], data["is_all_classroom"], classroom_uuid)
        assert r.get("msg") == "请绑定网关"
        # 删除教室
        r = self.classroom_manage.del_classroom(classroom_uuid)
        assert r.get("code") == 0
        # 删除地址
        r = self.addr_manage.del_address(addr_uuid)
        assert r.get("code") == 0

    @allure.story("获取设备集控websocket频道号测试用例")
    @allure.title("获取设备集控websocket频道号")
    @allure.severity("normal")
    @allure.description("获取设备集控websocket频道号")
    def test_get_websocket_channel(self):
        r = self.classroom_manage.get_websocket_channel()
        assert r.get("code") == 0
