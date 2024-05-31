# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class ResourceManageApi(BaseApi):
    def get_resource_list(self):
        """资源列表"""
        path = "backend/resource/list"
        return self.send("get", path)

    def resource_binding(self, target_type, target_uuid, uuid):
        """资源绑定"""
        path = "backend/resource/bind"
        data = {
            "targetType": target_type,
            "targetUuid": target_uuid,
            "uuid": uuid,
        }
        return self.send("post", path, json=data)

    def resource_unbinding(self):
        pass

    def resource_edit(self):
        pass

    def resource_delete(self):
        pass

    def resource_sorting(self):
        pass
