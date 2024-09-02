# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class RegManageApi(BaseApi):
    """报名管理模块"""

    def config_list(self):
        """配置列表"""
        path = "backend/collect/config-list"
        return self.send("get", path)

    def save_config_insert(self, insert):
        """保存配置新增数据"""
        path = "backend/collect/config-save"
        data = {
            "insert": insert
        }
        return self.send("post", path, json=data)

    def save_config_update(self, update):
        """编辑保存配置"""
        path = "backend/collect/config-save"
        data = {
            "update": update
        }
        return self.send("post", path, json=data)

    def save_config_delete(self, delete):
        """删除保存配置"""
        path = "backend/collect/config-save"
        data = {
            "delete": delete
        }
        return self.send("post", path, json=data)

    def add_registration(self, type, target_uuid, start_time, end_time, title, collectionConfig):
        """新增报名"""
        path = "backend/collect/insert"
        data = {
            "type": type,
            "target_uuid": target_uuid,
            "start_time": start_time,
            "end_time": end_time,
            "title": title,
            "collectionConfig": collectionConfig
        }
        return self.send("post", path, json=data)

    def registration_list(self):
        """"报名列表"""
        path = "backend/collect/list"
        return self.send("get", path)

    def del_registration(self, uuid):
        """删除报名采集"""
        path = "backend/collect/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def edit_registration(self, uuid, start_time, end_time, collectionConfig):
        """编辑报名"""
        path = "backend/collect/edit"
        data = {
            "uuid": uuid,
            "start_time": start_time,
            "end_time": end_time,
            "collectionConfig": collectionConfig
        }
        return self.send("post", path, json=data)

    def detail_registration(self, uuid):
        """报名详情"""
        path = "backend/collect/apply"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def export_reg_info(self):
        """导出报名信息"""
        path = "backend/collect/export"
        return self.send("get", path)
