# -*- coding: utf-8 -*-
import allure
import pytest
from api.ChatRoomManageApi import ChatRoomManageApi
from api.LiveManageApi import LiveManageApi
from api.UniversalApi import UniversalApi
from api.UserManageApi import UserManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("聊天室管理模块")
class TestChatRoomManageApi:

    def setup_class(self):
        self.chatroom = ChatRoomManageApi()
        self.live_manage = LiveManageApi()
        self.user_manage = UserManageApi()
        self.uni = UniversalApi()

    @allure.story("获取全部成员测试用例")
    @allure.title("获取全部成员")
    @allure.severity("normal")
    @allure.description("获取全部成员")
    @pytest.mark.parametrize("data", get_data()["get_all_members"])
    def test_get_all_members(self, data):
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
        # 编辑直播
        r = self.live_manage.update_live(live_uuid, data["title_update"], data["start_time"], data["end_time"],
                                         live_uuid,
                                         data['speaker_rooms']['org_id'], data['speaker_rooms']['room_id'],
                                         data['speaker_rooms']['room_uuid'], data['speaker_rooms']['room_name'],
                                         data['speaker_rooms']['title'], data['speaker_rooms']['mac'],
                                         data['speaker_rooms']['action'],
                                         data["playback_mode"], data["interactive_modes"], data["live_mode"],
                                         data["speaker_room_type"], data["listener_room_type"],
                                         data["push_source_type"], speaker_uuid, resource_uuid)
        assert r.get("code") == 0
        # 直播详情
        r = self.live_manage.live_detail(live_uuid)
        channel = JsonPathUtils.get(r, "$..channel")[0]
        self.chatroom.get_all_members(channel)
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0
