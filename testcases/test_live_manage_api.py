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
class TestLiveManageApi(BaseApi):

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

    @allure.story("直播编辑测试用例")
    @allure.title("直播编辑")
    @allure.severity("normal")
    @allure.description("直播编辑")
    @pytest.mark.parametrize("data", get_data()["update_live"])
    def test_update_live(self, data):
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
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0

    @allure.story("直播图文创建测试用例")
    @allure.title("直播图文创建")
    @allure.severity("normal")
    @allure.description("直播图文创建")
    @pytest.mark.parametrize("data", get_data()["create_image_text_live"])
    def test_create_image_text_live(self, data):
        # 查询用户自身信息
        r = self.user_manage.user_person_info()
        speaker_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 上传视频文件
        r = self.uni.upload_resource_live()
        resource_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建直播
        r = self.live_manage.live_create(data["title"], data["start_time"], data["end_time"],
                                         data['speaker_rooms']['org_id'], data['speaker_rooms']['room_id'],
                                         data['speaker_rooms']['room_uuid'],
                                         data['speaker_rooms']['room_name'],
                                         data['speaker_rooms']['title'], data['speaker_rooms']['mac'],
                                         data['speaker_rooms']['action'],
                                         data["playback_mode"], data["interactive_mode"], data["live_mode"],
                                         data["speaker_room_type"], data["listener_room_type"],
                                         data["push_source_type"], speaker_uuid, resource_uuid)
        assert r.get("code") == 0
        live_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 上传图片
        r = self.uni.upload_resource()
        image_url = JsonPathUtils.get(r, "$..url")[0]
        # 直播图文创建
        self.live_manage.create_image_text_live(live_uuid, data["enable_graphic"], data["introduce"], image_url)
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0

    @allure.story("直播图文删除测试用例")
    @allure.title("直播图文删除")
    @allure.severity("normal")
    @allure.description("直播图文删除")
    @pytest.mark.parametrize("data", get_data()["del_image_text_live"])
    def test_del_image_text_live(self, data):
        # 查询用户自身信息
        r = self.user_manage.user_person_info()
        speaker_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 上传视频文件
        r = self.uni.upload_resource_live()
        resource_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建直播
        r = self.live_manage.live_create(data["title"], data["start_time"], data["end_time"],
                                         data['speaker_rooms']['org_id'], data['speaker_rooms']['room_id'],
                                         data['speaker_rooms']['room_uuid'],
                                         data['speaker_rooms']['room_name'],
                                         data['speaker_rooms']['title'], data['speaker_rooms']['mac'],
                                         data['speaker_rooms']['action'],
                                         data["playback_mode"], data["interactive_mode"], data["live_mode"],
                                         data["speaker_room_type"], data["listener_room_type"],
                                         data["push_source_type"], speaker_uuid, resource_uuid)
        assert r.get("code") == 0
        live_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 上传图片
        r = self.uni.upload_resource()
        image_url = JsonPathUtils.get(r, "$..url")[0]
        # 直播图文创建
        r = self.live_manage.create_image_text_live(live_uuid, data["enable_graphic"], data["introduce"], image_url)
        assert r.get("code") == 0
        # 直播详情接口拿图文uuid
        r = self.live_manage.live_detail(live_uuid)
        text_uuid = JsonPathUtils.get(r, "$..graphic_list[0]..uuid")[0]
        # 删除图文直播
        self.live_manage.del_image_text_live(text_uuid)
        assert r.get("code") == 0
        # 删除直播
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0

    @allure.story("直播名称列表测试用例")
    @allure.title("直播名称列表")
    @allure.severity("normal")
    @allure.description("直播名称列表")
    def test_list_name(self):
        # 直播名称列表
        r = self.live_manage.list_name()
        assert r.get("code") == 0

    @allure.story("获取分享链接测试用例")
    @allure.title("获取分享链接")
    @allure.severity("normal")
    @allure.description("获取分享链接")
    @pytest.mark.parametrize("data", get_data()["get_share_link"])
    def test_get_share_link(self, data):
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
        # 获取分享链接
        r = self.live_manage.get_share_link(live_uuid)
        assert r.get("code") == 0
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0

    @allure.story("快速编辑测试用例")
    @allure.title("快速编辑")
    @allure.severity("normal")
    @allure.description("快速编辑")
    @pytest.mark.parametrize("data", get_data()["quick_edit"])
    def test_quick_edit(self, data):
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
        # 快速编辑
        r = self.live_manage.quick_edit(live_uuid, data["type"], data["value"])
        assert r.get("code") == 0
        r = self.live_manage.live_del(live_uuid)
        assert r.get("code") == 0
