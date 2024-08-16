# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class UserManageApi(BaseApi):
    """
    用户管理模块
    """

    def get_user_list(self, page, size):
        """获取用户列表"""
        data = {
            "page": page,
            "size": size
        }
        path = "backend/user/list"
        return self.send("get", path, params=data)

    def get_user_list_null(self):
        """获取用户列表不传递参数"""
        path = "backend/user/list"
        return self.send("get", path)

    def add_student(self, phone, name, pwd):
        """添加学生"""
        data = {
            "phone": phone,
            "name": name,
            "pwd": pwd
        }
        path = "backend/user/add-student"
        return self.send("post", path, json=data)

    def del_user(self, user_uuid):
        """删除用户"""
        data = {
            "user_uuid": user_uuid
        }
        path = "backend/v2/user/del"
        return self.send("post", path, json=data)

    def add_teacher(self, phone, name, identity, pwd):
        """添加老师"""
        data = {
            "phone": phone,
            "name": name,
            "identity": identity,
            "pwd": pwd
        }
        path = "backend/user/add-teacher"
        return self.send("post", path, json=data)

    def disable_user(self, uuid):
        """禁用用户"""
        data = {
            "uuid": uuid
        }
        path = "backend/user/disable"
        return self.send("post", path, json=data)

    def import_teacher(self):
        """导入老师"""
        path = "backend/user/import-teacher"
        files = {
            "upload-file": ("老师模版.xlsx",
                            # open(r"E:\python_project\own_project\web_ui\sass_apiauto\files\老师模版.xlsx", "rb"),
                            open(r"files/老师模版.xlsx", "rb"),
                            "application/octet-stream"
                            )
        }
        return self.send("post", path, files=files)

    def import_student(self):
        """导入学生"""
        path = "backend/user/import-student"
        files = {
            "upload-file": ("学生模版.xlsx",
                            # open(r"E:\python_project\own_project\web_ui\sass_apiauto\files\学生模版.xlsx", "rb"),
                            open(r"files/学生模版.xlsx", "rb"),
                            "application/octet-stream"
                            )
        }
        return self.send("post", path, files=files)

    def edit_user(self, uuid, nickname, phone, real_name, identities, gender, stu_no):
        """编辑用户"""
        path = "backend/user/modify-user"
        data = {
            "uuid": uuid,
            "nickname": nickname,
            "phone": phone,
            "real_name": real_name,
            "identities": identities,
            "gender": gender,
            "stu_no": stu_no
        }
        return self.send("post", path, json=data)

    def user_detail(self, uuid):
        """用户信息"""
        path = "backend/user/user-detail"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def add_user(self, phone, name, identities, pwd):
        """添加用户"""
        path = "backend/user/add-user"
        data = {
            "phone": phone,
            "name": name,
            "identities": identities,
            "pwd": pwd
        }
        return self.send("post", path, json=data)

    def unblock_users(self, uuid):
        """解封用户"""
        path = "backend/user/open"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def switching_identities(self, role_id):
        """切换角色"""
        path = "v2/user/switch-role"
        data = {
            "role_id": role_id
        }
        return self.send("post", path, json=data)

    def user_info(self):
        """用户接口信息"""
        path = "backend/user/info"
        return self.send("get", path)

    def user_person_info(self):
        """查询用户自身信息"""
        path = "v2/user/info"
        return self.send("get", path)
