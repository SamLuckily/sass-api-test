# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class GroupManageApi(BaseApi):
    """
    分组管理
    """

    def add_group_template(self, template_name, grade_uuid):
        """新增分组模板"""
        path = "backend/grade/group/template-insert"
        data = {
            "template_name": template_name,
            "grade_uuid": grade_uuid
        }
        return self.send("post", path, json=data)

    def edit_group_template(self, template_name, uuid):
        """编辑分组模板"""
        path = "backend/grade/group/template-edit"
        data = {
            "template_name": template_name,
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def del_group_template(self, uuid):
        """分组模板删除"""
        path = "backend/grade/group/template-delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def save_group_template(self, template_uuid, group_name):
        """保存分组以及分组成员"""
        path = "backend/grade/group/save"
        data = {
            "template_uuid": template_uuid,
            "group_name": group_name
        }
        return self.send("post", path, json=data)

    def save_group_templates(self, template_uuid, group_name, students):
        """保存分组以及分组成员-小组内添加学生"""
        path = "backend/grade/group/save"
        data = {
            "template_uuid": template_uuid,
            "group_name": group_name,
            "students": students
        }
        return self.send("post", path, json=data)

    def group_template_list(self, grade_uuid):
        """分组模板列表数据"""
        path = "backend/grade/group/templates"
        data = {
            "grade_uuid": grade_uuid
        }
        return self.send("get", path, params=data)

    def get_template_info(self, grade_uuid):
        """获取模板信息"""
        path = "backend/grade/group/templates"
        data = {
            "grade_uuid": grade_uuid
        }
        return self.send("get", path, params=data)

    def get_templates_details(self, uuid):
        """获取模板详情"""
        path = "backend/grade/group/detail"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def del_templates_group_info(self, group_uuid):
        """删除模板中的分组信息"""
        path = "backend/grade/group/delete"
        data = {
            "group_uuid": group_uuid
        }
        return self.send("post", path, json=data)

