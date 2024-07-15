# -*- coding: utf-8 -*-
import allure
import pytest
from api.BaseApi import BaseApi
from api.ChapterManageApi import ChapterManageApi
from api.CourseManageApi import CourseManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("课程章节管理模块")
class TestCourseChapterManagementApi(BaseApi):
    def setup_class(self):
        self.course_management = CourseManageApi()
        self.chapter_management = ChapterManageApi()

    @allure.story("章节新增测试用例")
    @allure.title("章节新增")
    @allure.severity('normal')
    @allure.description("章节新增")
    @pytest.mark.parametrize("data", get_data()['chapter_add'])
    def test_add_chapter(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("章节编辑测试用例")
    @allure.title("章节编辑")
    @allure.severity('normal')
    @allure.description("章节编辑")
    @pytest.mark.parametrize("data", get_data()['chapter_edit'])
    def test_edit_chapter(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        uuid_chapter = JsonPathUtils.get(r, "$..uuid")[0]
        self.chapter_management.chapter_edit(data['title'], uuid_chapter)
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("章节删除测试用例")
    @allure.title("章节删除")
    @allure.severity('normal')
    @allure.description("章节删除")
    @pytest.mark.parametrize("data", get_data()['chapter_delete'])
    def test_delete_chapter(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
        uuid_chapter = JsonPathUtils.get(r, "$..uuid")[0]
        self.chapter_management.chapter_delete(uuid_chapter)
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("章节列表测试用例")
    @allure.title("章节列表")
    @allure.severity('normal')
    @allure.description("章节列表")
    @pytest.mark.parametrize("data", get_data()['chapter_list'])
    def test_list_chapter(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_list(course_uuid)
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("章节排序测试用例")
    @allure.title("章节排序")
    @allure.severity('normal')
    @allure.description("章节排序")
    @pytest.mark.parametrize("data", get_data()['chapter_sort'])
    def test_sort_chapter(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add(data["name_chapter_one"], course_uuid)
        uuid_chapter_one = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add(data["name_chapters_two"], course_uuid)
        r = self.chapter_management.chapter_add(data["name_chapters_three"], course_uuid)
        uuid_chapter_two = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_sorting(data["sort_two"], uuid_chapter_one, course_uuid)
        r = self.chapter_management.chapter_sorting(data["sort_one"], uuid_chapter_two, course_uuid)
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0
