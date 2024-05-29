# -*- coding: utf-8 -*-
import jsonpath
from api.BaseApi import BaseApi
from api.ChapterManagementApi import ChapterManagementApi
from api.CourseManagementApi import CourseManagementApi
from api.LessonManagementApi import LessonManagementApi
from api.ResourceManagementApi import ResourceManagementApi
from api.UniversalApi import UniversalApi
from utils.jsonpath_utils import JsonPathUtils


class TestResourceManagementApi(BaseApi):
    def setup_class(self):
        self.resource_management = ResourceManagementApi()
        self.course_management = CourseManagementApi()
        self.chapter_management = ChapterManagementApi()
        self.lessonManagement = LessonManagementApi()
        self.universal = UniversalApi()

    def test_get_resource_list(self):
        """获取资源列表"""
        code = self.resource_management.get_resource_list().get("code")
        assert code == 0

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
        assert r.get("code") == 0
        assert code

    def test_resource_unbinding(self):
        assert False

    def test_resource_edit(self):
        assert False

    def test_resource_delete(self):
        assert False

    def test_resource_sorting(self):
        assert False
