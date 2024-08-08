# -*- coding: utf-8 -*-
import allure
import pytest
from api.BaseApi import BaseApi
from api.UserManageApi import UserManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("用户管理模块")
class TestUserManageApi(BaseApi):
    def setup_class(self):
        self.user_manage = UserManageApi()

    @allure.story("获取用户列表测试用例")
    @allure.title("获取用户列表")
    @allure.severity('normal')
    @allure.description("获取用户列表")
    @pytest.mark.parametrize("data", get_data()['get_user_list'])
    def test_get_user_list(self, data):
        r = self.user_manage.get_user_list(data["page"], data["size"])
        assert r.get("msg") == "success"

    @allure.story("添加学生测试用例")
    @allure.title("添加学生")
    @allure.severity("normal")
    @allure.description("添加学生")
    @pytest.mark.parametrize("data", get_data()["add_student"])
    def test_add_student(self, data):
        self.user_manage.add_student(data["phone"], data["names"], data["pwd"])
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("添加学生输入异常手机号测试用例")
    @allure.title("添加学生输入异常手机号")
    @allure.severity("normal")
    @allure.description("添加学生输入异常手机号")
    @pytest.mark.parametrize("data", get_data()["add_student_phone"])
    def test_add_student_phone(self, data):
        r = self.user_manage.add_student(data["phone"], data["names"], data["pwd"])
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 51
        assert len(code) == 1 and code[0] == 51

    @allure.story("添加老师测试用例")
    @allure.title("添加老师")
    @allure.severity("normal")
    @allure.description("添加老师")
    @pytest.mark.parametrize("data", get_data()["add_teacher"])
    def test_add_teacher(self, data):
        self.user_manage.add_teacher(data["phone"], data["names"], data["identity"], data["pwd"])
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("禁用用户测试用例")
    @allure.title("禁用用户")
    @allure.severity("normal")
    @allure.description("禁用用户")
    @pytest.mark.parametrize("data", get_data()["add_teacher"])
    def test_disable_user(self, data):
        self.user_manage.add_teacher(data["phone"], data["names"], data["identity"], data["pwd"])
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        self.user_manage.disable_user(user_uuid)
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("导入老师测试用例")
    @allure.title("导入老师")
    @allure.severity("normal")
    @allure.description("导入老师")
    def test_import_teacher(self):
        self.user_manage.import_teacher()
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("导入已存在老师测试用例")
    @allure.title("导入已存在老师")
    @allure.severity("normal")
    @allure.description("导入已存在老师")
    def test_import_teacher_double(self):
        self.user_manage.import_teacher()
        r = self.user_manage.import_teacher()
        err_count = JsonPathUtils.get(r, "$..err_count")
        assert len(err_count) == 1 and err_count[0] == 1
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("导入学生测试用例")
    @allure.title("导入学生")
    @allure.severity("normal")
    @allure.description("导入学生")
    def test_import_student(self):
        self.user_manage.import_student()
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("导入已存在学生测试用例")
    @allure.title("导入已存在学生")
    @allure.severity("normal")
    @allure.description("导入已存在学生")
    def test_import_student_double(self):
        self.user_manage.import_student()
        r = self.user_manage.import_student()
        err_count = JsonPathUtils.get(r, "$..err_count")
        assert len(err_count) == 1 and err_count[0] == 1
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("编辑用户测试用例")
    @allure.title("编辑用户")
    @allure.severity("normal")
    @allure.description("编辑用户")
    @pytest.mark.parametrize("data", get_data()["edit_user"])
    def test_edit_user(self, data):
        self.user_manage.import_student()
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        self.user_manage.edit_user(user_uuid, data["nickname"], data["phone"], data["real_name"], data["identities"],
                                   data["gender"], data["stu_no"])
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("编辑用户手机号为异常号码测试用例")
    @allure.title("编辑用户手机号为异常号码")
    @allure.severity("normal")
    @allure.description("编辑用户手机号为异常号码")
    @pytest.mark.parametrize("data", get_data()["edit_user_phone"])
    def test_edit_user(self, data):
        self.user_manage.import_student()
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        self.user_manage.edit_user(user_uuid, data["nickname"], data["phone"], data["real_name"], data["identities"],
                                   data["gender"], data["stu_no"])
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("编辑用户角色为不存在角色测试用例")
    @allure.title("编辑用户角色为不存在角色")
    @allure.severity("normal")
    @allure.description("编辑用户角色为不存在角色")
    @pytest.mark.parametrize("data", get_data()["edit_user_identities"])
    def test_edit_user(self, data):
        self.user_manage.import_student()
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.edit_user(user_uuid, data["nickname"], data["phone"], data["real_name"],
                                       data["identities"],
                                       data["gender"], data["stu_no"])
        msg = JsonPathUtils.get(r, "$..msg")[0]
        assert msg == "角色不存在"
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("获取用户信息测试用例")
    @allure.title("获取用户信息")
    @allure.severity("normal")
    @allure.description("获取用户信息")
    def test_user_detail(self):
        self.user_manage.import_student()
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        self.user_manage.user_detail(user_uuid)
        code = JsonPathUtils.get(r, "$..code")[0]
        assert code == 0
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("添加用户测试用例")
    @allure.title("添加用户")
    @allure.severity("normal")
    @allure.description("添加用户")
    @pytest.mark.parametrize("data", get_data()["add_user"])
    def test_add_user(self, data):
        r = self.user_manage.add_user(data["phone"], data["names"], data["identities"], data["pwd"])
        assert r.get("code") == 0
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("解禁用户测试用例")
    @allure.title("解禁用户")
    @allure.severity("normal")
    @allure.description("解禁用户")
    @pytest.mark.parametrize("data", get_data()["add_user"])
    def test_unblock_user(self, data):
        r = self.user_manage.add_user(data["phone"], data["names"], data["identities"], data["pwd"])
        assert r.get("code") == 0
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        r = self.user_manage.get_user_list(page, size)
        user_uuid = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        r = self.user_manage.disable_user(user_uuid)
        assert r.get("code") == 0
        r = self.user_manage.unblock_users(user_uuid)
        assert r.get("code") == 0
        r = self.user_manage.del_user(user_uuid)
        code = JsonPathUtils.get(r, "$..code")
        # 断言
        assert r.get("code") == 0
        assert len(code) == 1 and code[0] == 0

    @allure.story("用户信息接口测试用例")
    @allure.title("用户信息接口")
    @allure.severity("normal")
    @allure.description("用户信息接口")
    def test_switching_identities_teacher(self):
        r = self.user_manage.user_info()
        assert r.get("code") == 0






