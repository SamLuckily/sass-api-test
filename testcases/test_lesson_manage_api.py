# -*- coding: utf-8 -*-
from time import sleep

import allure
import pytest
from api.BaseApi import BaseApi
from api.ChapterManageApi import ChapterManageApi
from api.CourseManageApi import CourseManageApi
from api.LessonManageApi import LessonManageApi
from api.ResourceManageApi import ResourceManageApi
from api.UniversalApi import UniversalApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("课时管理模块")
class TestLessonManagementApi(BaseApi):
    def setup_class(self):
        self.resource_management = ResourceManageApi()
        self.course_management = CourseManageApi()
        self.chapter_management = ChapterManageApi()
        self.lesson_management = LessonManageApi()
        self.universal = UniversalApi()

    @allure.story("新增课时测试用例")
    @allure.title("新增课时")
    @allure.severity('normal')
    @allure.description("新增课时")
    @pytest.mark.parametrize("data", get_data()['lesson_add'])
    def test_add_lesson(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.lesson_management.lesson_add(data['name_lesson'], course_uuid, chapter_uuid, data["view"])
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("课时编辑测试用例")
    @allure.title("课时编辑")
    @allure.severity('normal')
    @allure.description("课时编辑")
    @pytest.mark.parametrize("data", get_data()['lesson_edit'])
    def test_edit_lesson(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.lesson_management.lesson_add(data['name_lesson'], course_uuid, chapter_uuid, data["view"])
        lesson_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.lesson_management.lesson_edit(lesson_uuid, data["edit_name_lesson"])
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0
