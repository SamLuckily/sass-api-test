# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class ResourceManageApi(BaseApi):
    """
    资源管理
    """
    def get_resource_list(self):
        """获取资源列表"""
        path = "backend/resource/list"
        return self.send("get", path)

    def resource_binding(self, target_type, target_uuid, uuid):
        """资源绑定"""
        path = "backend/resource/bind"
        data = {
            "targetType": target_type,
            "targetUuid": target_uuid,
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def resource_unbinding(self, target_type, target_uuid, uuid):
        """资源解除绑定"""
        path = "backend/resource/unbind"
        data = {
            "targetType": target_type,
            "targetUuid": target_uuid,
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def resource_edit(self, file_name, uuid):
        """资源编辑"""
        path = "backend/resource/edit"
        data = {
            "name": file_name,
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def resource_delete(self, uuid):
        """资源删除"""
        path = "backend/resource/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def resource_sorting(self, uuid, belong_id, sort):
        """资源排序"""
        path = "backend/resource/sort"
        data = {
            "uuid": uuid,
            "belong_id": belong_id,
            "sort": sort
        }
        return self.send("post", path, json=data)
