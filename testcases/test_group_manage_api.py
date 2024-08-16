# -*- coding: utf-8 -*-
import allure
import pytest

from api.BaseApi import BaseApi
from api.ClassManagementApi import ClassManageApi
from api.GroupManagementApi import GroupManageApi
from api.UserManageApi import UserManageApi
from testcases.conftest import get_data
from utils.jsonpath_utils import JsonPathUtils


@allure.feature("分组管理模块")
class TestGroupManage(BaseApi):
    def setup_class(self):
        self.group_manage = GroupManageApi()
        self.class_manage = ClassManageApi()
        self.user_manage = UserManageApi()

    @allure.story("分组模板新增测试用例")
    @allure.title("分组模板新增")
    @allure.severity('normal')
    @allure.description("分组模板新增")
    @pytest.mark.parametrize("data", get_data()['add_group_template'])
    def test_add_group_template(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("编辑分组模板测试用例")
    @allure.title("编辑分组模板")
    @allure.severity('normal')
    @allure.description("编辑分组模板")
    @pytest.mark.parametrize("data", get_data()['edit_group_template'])
    def test_edit_group_template(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 编辑分组模板
        r = self.group_manage.edit_group_template(data["edit_template_name"], uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("分组模板删除测试用例")
    @allure.title("分组模板删除")
    @allure.severity('normal')
    @allure.description("分组模板删除")
    @pytest.mark.parametrize("data", get_data()['del_group_template'])
    def test_del_group_template(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 删除分组模板
        r = self.group_manage.del_group_template(uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("保存分组以及分组成员测试用例")
    @allure.title("保存分组以及分组成员")
    @allure.severity('normal')
    @allure.description("保存分组以及分组成员")
    @pytest.mark.parametrize("data", get_data()['save_group_template'])
    def test_save_group_template(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 保存分组以及分组成员
        r = self.group_manage.save_group_template(uuid, data["group_name"])
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("保存分组以及分组成员测试用例")
    @allure.title("保存分组以及分组成员")
    @allure.severity('normal')
    @allure.description("保存分组以及分组成员")
    @pytest.mark.parametrize("data", get_data()['save_group_templates'])
    def test_save_group_templates(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        template_uuid = JsonPathUtils.get(r, "$..uuid")[0]
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
        # 保存分组以及分组成员-小组内添加学生
        r = self.group_manage.save_group_templates(template_uuid, data["group_name"], user_uuid)
        assert r.get("code") == 0
        # 删除学生
        r = self.user_manage.del_user(user_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("分组模板列表数据测试用例")
    @allure.title("分组模板列表数据")
    @allure.severity('normal')
    @allure.description("分组模板列表数据")
    @pytest.mark.parametrize("data", get_data()['group_template_list'])
    def test_group_template_list(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 分组模板列表数据
        r = self.group_manage.group_template_list(class_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("获取模版信息测试用例")
    @allure.title("获取模版信息")
    @allure.severity('normal')
    @allure.description("获取模版信息")
    @pytest.mark.parametrize("data", get_data()['get_template_info'])
    def test_get_template_info(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        assert r.get("code") == 0
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        assert r.get("code") == 0
        # 获取模版信息
        r = self.group_manage.get_template_info(class_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("获取模版详情（携带分组信息）测试用例")
    @allure.title("获取模版详情（携带分组信息）")
    @allure.severity('normal')
    @allure.description("获取模版详情（携带分组信息）")
    @pytest.mark.parametrize("data", get_data()['get_templates_details'])
    def test_get_templates_details(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        template_uuid = JsonPathUtils.get(r, "$..uuid")[0]
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
        # 保存分组以及分组成员-小组内添加学生
        r = self.group_manage.save_group_templates(template_uuid, data["group_name"], user_uuid)
        assert r.get("code") == 0
        # 获取模板详情
        self.group_manage.get_templates_details(template_uuid)
        # 删除学生
        r = self.user_manage.del_user(user_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("删除模版中的分组信息测试用例")
    @allure.title("删除模版中的分组信息")
    @allure.severity('normal')
    @allure.description("删除模版中的分组信息")
    @pytest.mark.parametrize("data", get_data()['del_templates_group_info'])
    def test_del_templates_group_info(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        template_uuid = JsonPathUtils.get(r, "$..uuid")[0]
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
        # 保存分组以及分组成员-小组内添加学生
        r = self.group_manage.save_group_templates(template_uuid, data["group_name"], user_uuid)
        assert r.get("code") == 0
        # 获取模板详情
        r = self.group_manage.get_templates_details(template_uuid)
        group_uuid = JsonPathUtils.get(r, "$..group_uuid")[0]
        # 删除模版中的分组信息
        self.group_manage.del_templates_group_info(group_uuid)
        # 删除学生
        r = self.user_manage.del_user(user_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("获取分组的教室信息测试用例")
    @allure.title("获取分组的教室信息")
    @allure.severity('normal')
    @allure.description("获取分组的教室信息")
    def test_get_templates_group_info(self):
        # 获取分组的教室信息
        r = self.group_manage.get_templates_group_info()
        assert r.get("code") == 0

    @allure.story("清除模版中的分组信息测试用例")
    @allure.title("清除模版中的分组信息")
    @allure.severity('normal')
    @allure.description("清除模版中的分组信息")
    @pytest.mark.parametrize("data", get_data()['clear_templates_group_info'])
    def test_clear_templates_group_info(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 创建分组模板
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        template_uuid = JsonPathUtils.get(r, "$..uuid")[0]
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
        # 保存分组以及分组成员-小组内添加学生
        r = self.group_manage.save_group_templates(template_uuid, data["group_name"], user_uuid)
        assert r.get("code") == 0
        # 清除模板的分组信息
        r = self.group_manage.clear_templates_group_info(template_uuid)
        assert r.get("code") == 0
        # 删除学生
        r = self.user_manage.del_user(user_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("将用户新增到多个分组中测试用例")
    @allure.title("将用户新增到多个分组中")
    @allure.severity('normal')
    @allure.description("将用户新增到多个分组中")
    @pytest.mark.parametrize("data", get_data()['add_user_groups'])
    def test_add_user_groups(self, data):
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 添加用户（学生一）
        self.user_manage.add_user(data["phone_one"], data["name_one"], data["identities"], data["pwd"])
        # 获取用户列表有多少页，每页显示多少数据
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        # 跳转到最后一页
        r_one = self.user_manage.get_user_list(page, size)
        # 获取最后一个学生的uuid
        user_one_uuid = JsonPathUtils.get(r_one, "$..list[(@.length-1)].uuid")[0]
        # 添加班级学生
        r = self.class_manage.add_class_students(class_uuid, user_one_uuid)
        assert r.get("code") == 0
        # 创建分组模板一
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        template_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 保存分组(创建小组)
        r = self.group_manage.save_group(template_uuid, data["group_name"])
        assert r.get("code") == 0
        # 创建分组模板二
        r = self.group_manage.add_group_template(data["template_names"], class_uuid)
        template_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 保存分组(创建小组)
        r = self.group_manage.save_group(template_uuid, data["group_names"])
        assert r.get("code") == 0
        # 获取模板信息
        r = self.group_manage.get_template_info(class_uuid)
        group_uuids = JsonPathUtils.get(r, "$..group_uuid")
        # 将用户新增到多个分组中
        r = self.group_manage.add_user_groups(class_uuid, group_uuids, user_one_uuid)
        assert r.get("code") == 0
        # 删除学生
        r = self.user_manage.del_user(user_one_uuid)
        assert r.get("code") == 0
        # 删除班级
        r = self.class_manage.delete_class(class_uuid)
        assert r.get("code") == 0

    @allure.story("分组模板小组学生移动测试用例")
    @allure.title("分组模板小组学生移动")
    @allure.severity('normal')
    @allure.description("分组模板小组学生移动")
    @pytest.mark.parametrize("data", get_data()['stu_move_in_group'])
    @pytest.mark.skip
    def test_stu_move_in_group(self, data):
        # 添加用户（学生一）
        self.user_manage.add_user(data["phone"], data["name"], data["identities"], data["pwd"])
        # 获取用户列表有多少页，每页显示多少数据
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        # 跳转到最后一页
        r_one = self.user_manage.get_user_list(page, size)
        # 获取最后一个学生的uuid
        user_uuid = JsonPathUtils.get(r_one, "$..list[(@.length-1)].uuid")[0]
        # 添加用户（学生二）
        self.user_manage.add_user(data["phones"], data["names"], data["identities"], data["pwd"])
        # 获取用户列表有多少页，每页显示多少数据
        r = self.user_manage.get_user_list_null()
        page = JsonPathUtils.get(r, "$..pagination.pages")
        size = JsonPathUtils.get(r, "$..pagination.size")
        # 跳转到最后一页
        r = self.user_manage.get_user_list(page, size)
        # 获取最后一个学生的uuid
        user_uuids = JsonPathUtils.get(r, "$..list[(@.length-1)].uuid")[0]
        # 新增班级
        r = self.class_manage.add_class(data["class_name"], self.access_token()[1])
        class_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 添加班级学生
        r = self.class_manage.add_class_students(class_uuid, f"{user_uuid},{user_uuids}")
        assert r.get("code") == 0
        # 创建分组模板一
        r = self.group_manage.add_group_template(data["template_name"], class_uuid)
        template_uuid = JsonPathUtils.get(r, "$..uuid")[0]
        # 保存分组(创建小组一)
        r = self.group_manage.save_group_templates(template_uuid, data["group_name"], user_uuid)
        assert r.get("code") == 0
        # 保存分组(创建小组二)
        r = self.group_manage.save_group_templates(template_uuid, data["group_names"], user_uuids)
        assert r.get("code") == 0
        # 获取模板信息
        r = self.group_manage.get_template_info(class_uuid)
        group_uuid = JsonPathUtils.get(r, "$..group_info[0].group_uuid")[0]
        # 获取模板详情（携带分组信息）
        r = self.group_manage.get_templates_details(template_uuid)
        user_uuid_g = JsonPathUtils.get(r, "$..group_info[1]..user_uuid")[0]
        group_name = JsonPathUtils.get(r, "$..group_info[0]..group_name")[0]
        # 分组模板小组学生移动
        self.group_manage.stu_move_in_group(template_uuid, group_uuid, group_name, user_uuid_g)
        # assert r.get("code") == 0
        # # 删除学生
        # self.user_manage.del_user(user_uuid)
        # self.user_manage.del_user(user_uuids)
        # # 删除班级
        # r = self.class_manage.delete_class(class_uuid)
        # assert r.get("code") == 0
