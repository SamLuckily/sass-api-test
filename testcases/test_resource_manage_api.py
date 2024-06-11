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


@allure.feature("资源管理模块")
class TestResourceManagementApi(BaseApi):
    def setup_class(self):
        self.resource_management = ResourceManageApi()
        self.course_management = CourseManageApi()
        self.chapter_management = ChapterManageApi()
        self.lessonManagement = LessonManageApi()
        self.universal = UniversalApi()

    @allure.story("获取资源列表测试用例")
    @allure.title("获取资源列表")
    @allure.severity('normal')
    @allure.description("获取资源列表")
    def test_get_resource_list_first(self):
        r = self.resource_management.get_resource_list()
        assert r.get("code") == 0

    # @allure.story("获取资源列表测试用例")
    # @allure.title("获取资源列表")
    # @allure.severity('normal')
    # @allure.description("获取资源列表")
    # def test_get_resource_lists(self):
    #     # 方式一：生成 jsonschema数据断言查询结果
    #     resource_list_jsonschema = JsonSchemaUtils.generate_jsonschema(self.resource_management.get_resource_list())
    #     logger.info(f"JSONSchema的结构为：{resource_list_jsonschema}")
    #     # 通过 schema 验证数据
    #     res = JsonSchemaUtils.validate_schema(self.resource_management.get_resource_list(), resource_list_jsonschema)
    #     logger.info(f"验证的结果为：{res}")
    #     assert res
    #
    # @allure.story("获取资源列表测试用例")
    # @allure.title("获取资源列表")
    # @allure.severity('normal')
    # @allure.description("获取资源列表")
    # def test_get_resource_list(self):
    #     # 方式二：使用jsonschema文件断言查询结果
    #     file_path = f"{Utils.get_root_path()}/data/resource_list.json"
    #     # 生成 schema 数据保存到文件中
    #     JsonSchemaUtils.generate_jsonschema_by_file(self.resource_management.get_resource_list(), file_path)
    #     # 通过文件验证数据
    #     res = JsonSchemaUtils.validate_schema_by_file(self.resource_management.get_resource_list(), file_path)
    #     logger.info(f"验证的结果为：{res}")
    #     assert res

    # @allure.story("资源绑定测试用例")
    # @allure.title("资源绑定")
    # @allure.severity('normal')
    # @allure.description("资源绑定")
    # @pytest.mark.parametrize("data", get_data()['resource_binding'])
    # def test_resource_binding(self, data):
    #     r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
    #                                           data["about"])
    #     course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
    #     chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.lessonManagement.lesson_add(data['name_lesson'], course_uuid, chapter_uuid, data['view'])
    #     lesson_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.universal.upload_resource()
    #     file_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     self.resource_management.resource_binding("course_lesson", lesson_uuid, file_uuid)
    #     self.course_management.course_delete(course_uuid)
    #     code = JsonPathUtils.get(r, "$..code")
    #     # 断言
    #     assert r.get("code") == 0
    #     assert len(code) == 1 and code[0] == 0
    #
    # @allure.story("资源解除绑定测试用例")
    # @allure.title("资源解除绑定")
    # @allure.severity('normal')
    # @allure.description("资源解除绑定")
    # @pytest.mark.parametrize("data", get_data()['resource_unbinding'])
    # def test_resource_unbinding(self, data):
    #     r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
    #                                           data["about"])
    #     course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
    #     chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.lessonManagement.lesson_add(data['name_lesson'], course_uuid, chapter_uuid, data['view'])
    #     lesson_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.universal.upload_resource()
    #     file_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     self.resource_management.resource_binding("course_lesson", lesson_uuid, file_uuid)
    #     self.resource_management.resource_unbinding("course_lesson", lesson_uuid, file_uuid)
    #     self.course_management.course_delete(course_uuid)
    #     code = JsonPathUtils.get(r, "$..code")
    #     # 断言
    #     assert r.get("code") == 0
    #     assert len(code) == 1 and code[0] == 0
    #
    # @allure.story("资源编辑测试用例")
    # @allure.title("资源编辑")
    # @allure.severity('normal')
    # @allure.description("资源编辑")
    # @pytest.mark.parametrize("data", get_data()['resource_edit'])
    # def test_resource_edit(self, data):
    #     """资源编辑"""
    #     r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
    #                                           data["about"])
    #     course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
    #     chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.lessonManagement.lesson_add(data['name_lesson'], course_uuid, chapter_uuid, data['view'])
    #     lesson_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.universal.upload_resource()
    #     file_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     self.resource_management.resource_binding("course_lesson", lesson_uuid, file_uuid)
    #     self.resource_management.resource_edit(data['file_name'], file_uuid)
    #     self.course_management.course_delete(course_uuid)
    #     code = JsonPathUtils.get(r, "$..code")
    #     # 断言
    #     assert r.get("code") == 0
    #     assert len(code) == 1 and code[0] == 0
    #
    # @allure.story("资源删除测试用例")
    # @allure.title("资源删除")
    # @allure.severity('normal')
    # @allure.description("资源删除")
    # @pytest.mark.parametrize("data", get_data()['resource_delete'])
    # def test_resource_delete(self, data):
    #     r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
    #                                           data["about"])
    #     course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
    #     chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.lessonManagement.lesson_add(data['name_lesson'], course_uuid, chapter_uuid, data['view'])
    #     lesson_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.universal.upload_resource()
    #     file_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     self.resource_management.resource_binding("course_lesson", lesson_uuid, file_uuid)
    #     self.resource_management.resource_unbinding("course_lesson", lesson_uuid, file_uuid)
    #     self.resource_management.resource_delete(file_uuid)
    #     self.course_management.course_delete(course_uuid)
    #     code = JsonPathUtils.get(r, "$..code")
    #     # 断言
    #     assert r.get("code") == 0
    #     assert len(code) == 1 and code[0] == 0
    #
    # @allure.story("资源排序测试用例")
    # @allure.title("资源排序")
    # @allure.severity('normal')
    # @allure.description("资源排序")
    # @pytest.mark.parametrize("data", get_data()['resource_sort'])
    # def test_resource_sorting(self, data):
    #     r = self.course_management.course_add(data['class_name'], self.access_token()[1], data['publish'],
    #                                           data["about"])
    #     course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.chapter_management.chapter_add(data["name_chapter"], course_uuid)
    #     chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.lessonManagement.lesson_add(data['name_lesson'], course_uuid, chapter_uuid, data['view'])
    #     lesson_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     r = self.universal.upload_resource()
    #     file_uuid = JsonPathUtils.get(r, "$..uuid")[0]
    #     self.resource_management.resource_binding("course_lesson", lesson_uuid, file_uuid)
    #     r = self.universal.upload_resource()
    #     file_uuids = JsonPathUtils.get(r, "$..uuid")[0]
    #     self.resource_management.resource_binding("course_lesson", lesson_uuid, file_uuids)
    #     r = self.course_management.course_details(course_uuid)
    #     belong_id = JsonPathUtils.get(r, "$..resource[0].belong_id")[0]
    #     self.resource_management.resource_sorting(file_uuid, belong_id, data['sort'])
    #     self.course_management.course_delete(course_uuid)
    #     code = JsonPathUtils.get(r, "$..code")
    #     # 断言
    #     assert r.get("code") == 0
    #     assert len(code) == 1 and code[0] == 0
