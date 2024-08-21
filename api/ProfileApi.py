# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class ProfileApi(BaseApi):
    """情景模式模块"""

    def profile(self):
        """获取情景模式列表"""
        path = "backend/scene-mode/list"
        return self.send("get", path)

    def add_profile(self, title, setting):
        """添加情景模式"""
        path = "backend/scene-mode/add"
        data = {
            "title": title,
            "setting": setting
        }
        return self.send("post", path, json=data)

    def del_profile(self, uuid):
        """删除情景模式"""
        path = "backend/scene-mode/del"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def edit_profile(self, uuid, title, setting):
        """编辑情景模式"""
        path = "backend/scene-mode/edit"
        data = {
            "uuid": uuid,
            "title": title,
            "setting": setting
        }
        return self.send("post", path, json=data)
