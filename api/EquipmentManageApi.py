# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class EquipmentManageApi(BaseApi):
    """
    设备管理
    """

    def equipment_list(self, page, size):
        """设备列表(带绑定状态)"""
        path = "backend/device/list"
        data = {
            "page": page,
            "size": size
        }
        return self.send("get", path, params=data)

    def equipment_list_display(self, page, size):
        """设备列表(下拉框展示)"""
        path = "backend/device/simple-list"
        data = {
            "page": page,
            "size": size
        }
        return self.send("get", path, params=data)
