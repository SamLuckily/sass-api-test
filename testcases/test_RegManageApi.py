# -*- coding: utf-8 -*-
import json

import allure
import pytest
from api.BaseApi import BaseApi
from api.ChapterManageApi import ChapterManageApi
from api.CourseManageApi import CourseManageApi
from api.LessonManageApi import LessonManageApi
from api.RegManageApi import RegManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils
from utils.time_stamp_utils import TimeStampUtils


@allure.feature("配置列表")
class TestRegManageApi(BaseApi):

    def setup_class(self):
        self.reg_manage = RegManageApi()
        self.course_management = CourseManageApi()
        self.chapter_management = ChapterManageApi()
        self.lesson_management = LessonManageApi()
        self.timestamp = TimeStampUtils()

    @allure.story("配置列表测试用例")
    @allure.title("配置列表")
    @allure.severity("normal")
    @allure.description("配置列表")
    def test_config_list(self):
        r = self.reg_manage.config_list()
        assert r.get("code") == 0

    @allure.story("保存配置测试用例")
    @allure.title("保存配置")
    @allure.severity("normal")
    @allure.description("保存配置")
    def test_save_config(self):
        insert = [
            {"title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_insert(insert)
        assert r.get("code") == 0
        r = self.reg_manage.config_list()
        uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        update = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;旅游;"}
        ]
        r = self.reg_manage.save_config_update(update)
        assert r.get("code") == 0
        delete = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;旅游;"}
        ]
        r = self.reg_manage.save_config_delete(delete)
        assert r.get("code") == 0

    @allure.story("新增报名（绑定课程或者直播）测试用例")
    @allure.title("新增报名（绑定课程或者直播）")
    @allure.severity("normal")
    @allure.description("新增报名（绑定课程或者直播）")
    @pytest.mark.parametrize("data", get_data()['add_registration'])
    def test_add_registration(self, data):
        # 新增课程
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        assert r.get("code") == 0
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 课程列表获取新增课程uuid
        r = self.course_management.course_list()
        course_name = JsonPathUtils.get(r, "$..list[0]..course_name")[0]
        # 新增章节
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 新增课时
        self.lesson_management.lesson_add(data["name_lesson"], course_uuid, chapter_uuid, data["view"])
        # 新增报名配置
        insert = [
            {"title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_insert(insert)
        assert r.get("code") == 0
        # 报名配置列表获取新增uuid
        r = self.reg_manage.config_list()
        uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 新增报名采集
        collectionConfig = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        start_time = self.timestamp.get_current_time()[0]
        end_time = self.timestamp.get_current_time()[1]
        self.reg_manage.add_registration(data["type"], course_uuid, start_time, end_time, course_name, collectionConfig)
        # 报名列表
        r = self.reg_manage.registration_list()
        assert r.get("code") == 0
        reg_list_uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 删除报名配置
        delete = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_delete(delete)
        assert r.get("code") == 0
        # 删除报名采集
        r = self.reg_manage.del_registration(reg_list_uuid)
        assert r.get("code") == 0
        # 删除课程
        r = self.course_management.course_delete(course_uuid)
        assert r.get("code") == 0

    @allure.story("编辑报名测试用例")
    @allure.title("编辑报名")
    @allure.severity("normal")
    @allure.description("编辑报名")
    @pytest.mark.parametrize("data", get_data()['edit_registration'])
    def test_edit_registration(self, data):
        # 新增课程
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 课程列表获取新增课程uuid
        r = self.course_management.course_list()
        course_name = JsonPathUtils.get(r, "$..list[0]..course_name")[0]
        # 新增章节
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 新增课时
        self.lesson_management.lesson_add(data["name_lesson"], course_uuid, chapter_uuid, data["view"])
        # 新增报名配置
        insert = [
            {"title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_insert(insert)
        assert r.get("code") == 0
        # 报名配置列表获取新增uuid
        r = self.reg_manage.config_list()
        uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 新增报名采集
        collectionConfig = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        start_time = self.timestamp.get_current_time()[0]
        end_time = self.timestamp.get_current_time()[1]
        self.reg_manage.add_registration(data["type"], course_uuid, start_time, end_time, course_name, collectionConfig)
        # 报名列表
        r = self.reg_manage.registration_list()
        assert r.get("code") == 0
        reg_list_uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 编辑报名
        r = self.reg_manage.edit_registration(reg_list_uuid, start_time, end_time, collectionConfig)
        assert r.get("code") == 0
        # 删除报名配置
        delete = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_delete(delete)
        assert r.get("code") == 0
        # 删除报名采集
        r = self.reg_manage.del_registration(reg_list_uuid)
        assert r.get("code") == 0
        # 删除课程
        r = self.course_management.course_delete(course_uuid)
        assert r.get("code") == 0

    @allure.story("报名详情测试用例")
    @allure.title("报名详情")
    @allure.severity("normal")
    @allure.description("报名详情")
    @pytest.mark.parametrize("data", get_data()['detail_registration'])
    def test_detail_registration(self, data):
        # 新增课程
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 课程列表获取新增课程uuid
        r = self.course_management.course_list()
        course_name = JsonPathUtils.get(r, "$..list[0]..course_name")[0]
        # 新增章节
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 新增课时
        self.lesson_management.lesson_add(data["name_lesson"], course_uuid, chapter_uuid, data["view"])
        # 新增报名配置
        insert = [
            {"title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_insert(insert)
        assert r.get("code") == 0
        # 报名配置列表获取新增uuid
        r = self.reg_manage.config_list()
        uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 新增报名采集
        collectionConfig = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        start_time = self.timestamp.get_current_time()[0]
        end_time = self.timestamp.get_current_time()[1]
        self.reg_manage.add_registration(data["type"], course_uuid, start_time, end_time, course_name, collectionConfig)
        # 报名列表
        r = self.reg_manage.registration_list()
        assert r.get("code") == 0
        reg_list_uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 报名详情（用户报名信息）
        r = self.reg_manage.detail_registration(reg_list_uuid)
        assert r.get("code") == 0
        # 删除报名配置
        delete = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_delete(delete)
        assert r.get("code") == 0
        # 删除报名采集
        r = self.reg_manage.del_registration(reg_list_uuid)
        assert r.get("code") == 0
        # 删除课程
        r = self.course_management.course_delete(course_uuid)
        assert r.get("code") == 0

    @pytest.mark.skip
    @allure.story("导出报名测试用例")
    @allure.title("导出报名")
    @allure.severity("normal")
    @allure.description("导出报名")
    @pytest.mark.parametrize("data", get_data()['export_reg_info'])
    def test_export_reg_info(self, data):
        # 新增课程
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 课程列表获取新增课程uuid
        r = self.course_management.course_list()
        course_name = JsonPathUtils.get(r, "$..list[0]..course_name")[0]
        # 新增章节
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 新增课时
        self.lesson_management.lesson_add(data["name_lesson"], course_uuid, chapter_uuid, data["view"])
        # 新增报名配置
        insert = [
            {"title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_insert(insert)
        assert r.get("code") == 0
        # 报名配置列表获取新增uuid
        r = self.reg_manage.config_list()
        uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 新增报名采集
        collectionConfig = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        start_time = self.timestamp.get_current_time()[0]
        end_time = self.timestamp.get_current_time()[1]
        self.reg_manage.add_registration(data["type"], course_uuid, start_time, end_time, course_name, collectionConfig)
        # 报名列表
        r = self.reg_manage.registration_list()
        assert r.get("code") == 0
        reg_list_uuid = JsonPathUtils.get(r, "$..list[0].uuid")[0]
        # 导出报名信息
        r = self.reg_manage.export_reg_info()
        assert r.get("code") == 0
        # 删除报名配置
        delete = [
            {"uuid": uuid, "title": "我的爱好", "isOption": 1, "optionContent": "睡觉;吃饭;躺平;"}
        ]
        r = self.reg_manage.save_config_delete(delete)
        assert r.get("code") == 0
        # 删除报名采集
        r = self.reg_manage.del_registration(reg_list_uuid)
        assert r.get("code") == 0
        # 删除课程
        r = self.course_management.course_delete(course_uuid)
        assert r.get("code") == 0
