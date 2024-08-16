# -*- coding: utf-8 -*-
import allure
import pytest

from api.BaseApi import BaseApi
from api.LiveManageApi import LiveManageApi
from api.UniversalApi import UniversalApi
from api.UserManageApi import UserManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("直播管理模块")
class TestLiveManageApiA(BaseApi):

    def setup_class(self):
        self.live_manage = LiveManageApi()
        self.user_manage = UserManageApi()
        self.uni = UniversalApi()

    @allure.story("直播列表测试用例")
    @allure.title("直播列表")
    @allure.severity("normal")
    @allure.description("直播列表")
    @pytest.mark.parametrize("data", get_data()["live_list"])
    def test_live_list(self, data):
        r = self.live_manage.live_list(data["page"], data["size"])
        assert r.get("code") == 0

    @allure.story("视频直播创建测试用例")
    @allure.title("视频直播创建")
    @allure.severity("normal")
    @allure.description("视频直播创建")
    @pytest.mark.parametrize("data", get_data()["create_live"])
    def test_crate_live(self, data):
        # 查询用户自身信息
        r = self.user_manage.user_person_info()
        speaker_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 上传视频文件
        r = self.uni.upload_resource_live()
        resource_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建直播
        r = self.live_manage.live_create(data["title"], data["start_time"], data["end_time"],
                                         data['speaker_rooms']['org_id'], data['speaker_rooms']['room_id'],
                                         data['speaker_rooms']['room_uuid'], data['speaker_rooms']['room_name'],
                                         data['speaker_rooms']['title'], data['speaker_rooms']['mac'],
                                         data['speaker_rooms']['action'],
                                         data["playback_mode"], data["interactive_mode"], data["live_mode"],
                                         data["speaker_room_type"], data["listener_room_type"],
                                         data["push_source_type"], speaker_uuid, resource_uuid)
        assert r.get("code") == 0
        live_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0

    @allure.story("直播详情测试用例")
    @allure.title("直播详情")
    @allure.severity("normal")
    @allure.description("直播详情")
    @pytest.mark.parametrize("data", get_data()["create_live"])
    def test_live_detail(self, data):
        # 查询用户自身信息
        r = self.user_manage.user_person_info()
        speaker_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 上传视频文件
        r = self.uni.upload_resource_live()
        resource_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建直播
        r = self.live_manage.live_create(data["title"], data["start_time"], data["end_time"],
                                         data['speaker_rooms']['org_id'], data['speaker_rooms']['room_id'],
                                         data['speaker_rooms']['room_uuid'], data['speaker_rooms']['room_name'],
                                         data['speaker_rooms']['title'], data['speaker_rooms']['mac'],
                                         data['speaker_rooms']['action'],
                                         data["playback_mode"], data["interactive_mode"], data["live_mode"],
                                         data["speaker_room_type"], data["listener_room_type"],
                                         data["push_source_type"], speaker_uuid, resource_uuid)
        live_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.live_manage.live_detail(live_uuid)
        assert r.get("code") == 0
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0

