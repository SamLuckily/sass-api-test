# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class SystemManagementApi(BaseApi):
    """
    系统管理
    """

    def homepage_config_save(self):
        """主页配置保存"""
        path = "v1/user/save-config"
        return self.send("post", path)
