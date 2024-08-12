# -*- coding: utf-8 -*-
import allure
import pytest

from api.BaseApi import BaseApi
from api.CourseManageApi import CourseManageApi
from api.UserManageApi import UserManageApi
from api.class_managementApi import ClassManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("班级管理模块")
class TestClassManageApi(BaseApi):
    def setup_class(self):
        self.class_manage = ClassManageApi()
        self.course_manage = CourseManageApi()
        self.user_manage = UserManageApi()

    @allure.story("班级新增测试用例")
    @allure.title("班级新增")
    @allure.severity('normal')
    @allure.description("班级新增")
    @pytest.mark.parametrize("data", get_data()['add_class'])
    def test_add_class(self, data):
        r = self.class_manage.add_class(data["name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.class_manage.delete_class(class_uuid)
        code = JsonPathUtils.get(r, "$..code")
        assert len(code) == 1 and code[0] == 0

    @allure.story("新增已存在班级测试用例")
    @allure.title("新增已存在班级")
    @allure.severity('normal')
    @allure.description("新增已存在班级")
    @pytest.mark.parametrize("data", get_data()['add_repeat_class'])
    def test_add_class_exist(self, data):
        r = self.class_manage.add_class(data["add_name"], self.access_token()[1])
        assert r.get("code") == 0
        repeat = self.class_manage.add_class(data["add_repeat_class"], self.access_token()[1])
        assert repeat.get("msg") == "相同班级信息已存在，请重新填写"
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.class_manage.delete_class(class_uuid)
        code = JsonPathUtils.get(r, "$..code")
        assert len(code) == 1 and code[0] == 0

    @allure.story("编辑班级测试用例")
    @allure.title("编辑班级")
    @allure.severity('normal')
    @allure.description("编辑班级")
    @pytest.mark.parametrize("data", get_data()['edit_class'])
    def test_edit_class(self, data):
        r = self.class_manage.add_class(data["add_name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.class_manage.edit_class(class_uuid, data["edit_name"], self.access_token()[1])
        assert r.get("code") == 0
        r = self.class_manage.delete_class(class_uuid)
        code = JsonPathUtils.get(r, "$..code")
        assert len(code) == 1 and code[0] == 0

    @allure.story("班级列表测试用例")
    @allure.title("班级列表")
    @allure.severity('normal')
    @allure.description("班级列表")
    def test_class_list(self):
        r = self.class_manage.class_list()
        assert r.get("code") == 0

    @allure.story("班级的课程名称列表测试用例")
    @allure.title("班级的课程名称列表")
    @allure.severity('normal')
    @allure.description("班级的课程名称列表，该班级下无课程")
    @pytest.mark.parametrize("data", get_data()['add_class'])
    def test_class_course_name_list(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["name"], self.access_token()[1])
        # 班级uuid
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 班级课程名称列表
        r = self.class_manage.class_course_name(class_uuid)
        assert r.get("code") == 0
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("班级的课程名称列表测试用例")
    @allure.title("班级的课程名称列表")
    @allure.severity('normal')
    @allure.description("班级的课程名称列表，该班级下有课程")
    @pytest.mark.parametrize("data", get_data()['course_class_add'])
    def test_class_course_name_lists(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 新增课程含班级
        r = self.course_manage.course_class_add(data["course_name"], self.access_token()[1], data["publish"],
                                                data["about"],
                                                class_uuid)
        course_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 班级课程名称列表（班级含课程）
        r = self.class_manage.class_course_name(class_uuid)
        assert r.get("code") == 0
        # 删除课程
        r = self.course_manage.course_delete(course_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("班级名称列表测试用例")
    @allure.title("班级名称列表")
    @allure.severity('normal')
    @allure.description("班级名称列表")
    def test_class_name_list(self):
        r = self.class_manage.class_name_list()
        assert r.get("code") == 0

    @allure.story("获取当前机构中未绑定班级的学生测试用例")
    @allure.title("获取当前机构中未绑定班级的学生")
    @allure.severity('normal')
    @allure.description("获取当前机构中未绑定班级的学生")
    def test_unbound_classes_student(self):
        r = self.class_manage.unbound_classes_student()
        assert r.get("code") == 0

    @allure.story("获取班级下的学生列表测试用例")
    @allure.title("获取班级下的学生列表")
    @allure.severity('normal')
    @allure.description("获取班级下的学生列表,该班级无学生")
    @pytest.mark.parametrize("data", get_data()['add_class'])
    def test_get_student_list_class(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        r = self.class_manage.get_student_list_class(class_uuid)
        assert r.get("code") == 0
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("添加班级学生测试用例")
    @allure.title("添加班级学生")
    @allure.severity('normal')
    @allure.description("添加班级学生")
    @pytest.mark.parametrize("data", get_data()['add_class_student'])
    def test_add_class_student(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 添加用户（学生）
        self.user_manage.add_user(data["phone"], data["names"], data["identities"], data["pwd"])
        # 获取用户列表有多少页，每页显示多少数据
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        # 跳转到最后一页
        r = self.user_manage.get_user_list(page, size)
        # 获取最后一个学生的uuid
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        # 添加班级学生
        r = self.class_manage.add_class_students(class_uuid, user_uuid)
        assert r.get("code") == 0
        # 删除学生
        self.user_manage.del_user(user_uuid)
        assert r.get("code") == 0
        # 删除班级
        self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("删除班级学生测试用例")
    @allure.story("删除班级学生")
    @allure.title("删除班级学生")
    @allure.severity('normal')
    @allure.description("删除班级学生")
    @pytest.mark.parametrize("data", get_data()['del_class_student'])
    def test_del_class_student(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 添加用户（学生）
        self.user_manage.add_user(data["phone"], data["names"], data["identities"], data["pwd"])
        # 获取用户列表有多少页，每页显示多少数据
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        # 跳转到最后一页
        r = self.user_manage.get_user_list(page, size)
        # 获取最后一个学生的uuid
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        # 添加班级学生
        r = self.class_manage.add_class_students(class_uuid, user_uuid)
        assert r.get("code") == 0
        # 删除班级学生
        r = self.class_manage.del_class_student(class_uuid, user_uuid)
        assert r.get("code") == 0
        # 删除学生
        self.user_manage.del_user(user_uuid)
        assert r.get("code") == 0
        # 删除班级
        self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("编辑班级学生测试用例")
    @allure.story("编辑班级学生")
    @allure.title("编辑班级学生")
    @allure.severity('normal')
    @allure.description("编辑班级学生")
    @pytest.mark.parametrize("data", get_data()['edit_class_student'])
    def test_edit_class_student(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 添加用户（学生）
        self.user_manage.add_user(data["phone"], data["names"], data["identities"], data["pwd"])
        # 获取用户列表有多少页，每页显示多少数据
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        # 跳转到最后一页
        r = self.user_manage.get_user_list(page, size)
        # 获取最后一个学生的uuid
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        # 添加班级学生
        r = self.class_manage.add_class_students(class_uuid, user_uuid)
        assert r.get("code") == 0
        # 编辑班级学生
        self.class_manage.edit_class_student(user_uuid, data["gender"])
        # 删除班级学生
        r = self.class_manage.del_class_student(class_uuid, user_uuid)
        assert r.get("code") == 0
        # 删除学生
        self.user_manage.del_user(user_uuid)
        assert r.get("code") == 0
        # 删除班级
        self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("班级老师列表测试用例")
    @allure.story("班级老师列表")
    @allure.title("班级老师列表")
    @allure.severity('normal')
    @allure.description("班级老师列表")
    @pytest.mark.parametrize("data", get_data()['class_teacher_list'])
    def test_class_teacher_list(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        grade_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 班级老师列表
        self.class_manage.class_teacher_list(grade_uuid)
        assert r.get("code") == 0
        # 删除班级
        self.class_manage.delete_class(grade_uuid)
        assert r.get("code") == 0

    @allure.story("班级取消关联老师测试用例")
    @allure.story("班级取消关联老师")
    @allure.title("班级取消关联老师")
    @allure.severity('normal')
    @allure.description("班级取消关联老师")
    @pytest.mark.parametrize("data", get_data()['class_disassociation_teacher'])
    def test_class_disassociation_teacher(self, data):
        # 新增老师一
        r_one = self.user_manage.add_user(data["phone_one"], data["teacher_one"], data["identities"], data["pwd"])
        assert r_one.get("code") == 0
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid_one = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        # 新增老师二
        r_two = self.user_manage.add_user(data["phone_two"], data["teacher_two"], data["identities"], data["pwd"])
        assert r_two.get("code") == 0
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid_two = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        # 新增班级且关联新增的两位老师
        r = self.class_manage.add_class(data["class_name"], f"{user_uuid_one},{user_uuid_two}")
        assert r_two.get("code") == 0
        grade_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 取消关联的老师一
        r = self.class_manage.class_disassociation_teacher(grade_uuid, user_uuid_one)
        assert r.get("code") == 0
        # 删除班级
        self.class_manage.delete_class(grade_uuid)
        assert r.get("code") == 0
        # 删除新增的老师一和老师二
        self.user_manage.del_user(user_uuid_one)
        assert r.get("code") == 0
        self.user_manage.del_user(user_uuid_two)
        assert r.get("code") == 0

