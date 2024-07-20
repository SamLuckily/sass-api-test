# -*- coding: utf-8 -*-
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
from utils.jsonschema_utils import JsonSchemaUtils
from utils.log_utils import logger
from utils.read_utils import Utils


@allure.feature("课程管理模块")
class TestCourseManagementApi(BaseApi):
    def setup_class(self):
        self.resource_management = ResourceManageApi()
        self.course_management = CourseManageApi()
        self.chapter_management = ChapterManageApi()
        self.lessonManagement = LessonManageApi()
        self.universal = UniversalApi()

    @allure.story("新增课程测试用例")
    @allure.title("新增课程")
    @allure.severity('normal')
    @allure.description("新增课程")
    @pytest.mark.parametrize("data", get_data()['chapter_add'])
    def test_add_course(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("课程上下架测试用例")
    @allure.title("新增课程")
    @allure.severity('normal')
    @allure.description("课程上下架")
    @pytest.mark.parametrize("data", get_data()['course_on_off'])
    def test_on_off_course(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.course_management.course_on_and_off(course_uuid, data['status'])
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("课程编辑测试用例")
    @allure.title("课程编辑")
    @allure.severity('normal')
    @allure.description("课程编辑")
    @pytest.mark.parametrize("data", get_data()['course_edit'])
    def test_edit_course(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.course_management.course_edit(course_uuid, data['name_edit'])
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("课程删除测试用例")
    @allure.title("课程删除")
    @allure.severity('normal')
    @allure.description("课程删除")
    @pytest.mark.parametrize("data", get_data()['course_delete'])
    def test_edit_course(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data["about"])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        code = JsonPathUtils.get(r, "$..code")
        self.course_management.course_delete(course_uuid)
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("课程列表测试用例")
    @allure.title("课程列表")
    @allure.severity('normal')
    @allure.description("课程列表")
    def test_list_course(self):
        r = self.course_management.course_list()
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("课程详情测试用例")
    @allure.title("课程详情")
    @allure.severity('normal')
    @allure.description("课程详情")
    @pytest.mark.parametrize("data", get_data()['course_detail'])
    def test_detail_course(self, data):
        r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
                                              data['about'])
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.course_management.course_details(course_uuid)
        self.course_management.course_delete(course_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("获取教师信息测试用例")
    @allure.title("教师信息")
    @allure.severity('normal')
    @allure.description("获取教师信息")
    def test_get_teacher(self):
        r = self.course_management.get_teacher()
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("课程名称列表测试用例")
    @allure.title("课程名称列表")
    @allure.severity('normal')
    @allure.description("课程名称列表")
    def test_course_name_list(self):
        r = self.course_management.get_course_name_list()
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0
