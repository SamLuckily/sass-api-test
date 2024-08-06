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
        path = "/backend/user/list"
        return self.send("get", path, params=data)
