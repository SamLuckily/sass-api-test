# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi
from api.ChapterManageApi import ChapterManageApi
from api.CourseManageApi import CourseManageApi
from api.LessonManageApi import LessonManageApi
from api.ResourceManageApi import ResourceManageApi
from api.UniversalApi import UniversalApi
from utils.jsonpath_utils import JsonPathUtils
from utils.jsonschema_utils import JsonSchemaUtils
from utils.log_utils import logger
from utils.read_utils import Utils


class TestResourceManagementApi(BaseApi):
    def setup_class(self):
        self.resource_management = ResourceManageApi()
        self.course_management = CourseManageApi()
        self.chapter_management = ChapterManageApi()
        self.lessonManagement = LessonManageApi()
        self.universal = UniversalApi()

    def test_get_resource_lists(self):
        """获取资源列表"""
        code = self.resource_management.get_resource_list().get("code")
        assert code == 0
        # 方式一：生成 jsonschema数据断言查询结果
        resource_list_jsonschema = JsonSchemaUtils.generate_jsonschema(self.resource_management.get_resource_list())
        logger.info(f"JSONSchema的结构为：{resource_list_jsonschema}")
        # 通过 schema 验证数据
        res = JsonSchemaUtils.validate_schema(self.resource_management.get_resource_list(), resource_list_jsonschema)
        logger.info(f"验证的结果为：{res}")
        assert res

    def test_get_resource_list(self):
        """获取资源列表"""
        # 方式二：使用jsonschema文件断言查询结果
        file_path = f"{Utils.get_root_path()}/data/resource_list.json"
        # 生成 schema 数据保存到文件中
        JsonSchemaUtils.generate_jsonschema_by_file(self.resource_management.get_resource_list(), file_path)
        # 通过文件验证数据
        res = JsonSchemaUtils.validate_schema_by_file(self.resource_management.get_resource_list(), file_path)
        logger.info(f"验证的结果为：{res}")
        assert res

    def test_resource_binding(self):
        """资源绑定"""
        r = self.course_management.course_add("测试课程", self.access_token()[1], "publish", "测试课程")
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.chapter_management.chapter_add("测试章节", course_uuid)
        chapter_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.lessonManagement.lesson_add("测试课时", course_uuid, chapter_uuid, "1")
        lesson_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.universal.upload_resource()
        file_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        self.resource_management.resource_binding("course_lesson", lesson_uuid, file_uuid)
        self.course_management.course_delete(course_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    # def test_resource_unbinding(self):
    #     assert False
    #
    # def test_resource_edit(self):
    #     assert False
    #
    # def test_resource_delete(self):
    #     assert False
    #
    # def test_resource_sorting(self):
    #     assert False
