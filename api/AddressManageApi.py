# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class AddressManageApi(BaseApi):
    """地址管理模块"""

    def address_list(self):
        """地址列表"""
        path = "backend/location/list"
        return self.send("get", path)

    def add_address(self, title):
        """添加地址"""
        path = "backend/location/add"
        data = {
            "title": title
        }
        return self.send("post", path, json=data)

    def del_address(self, uuid):
        """删除地址"""
        path = "backend/location/del"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def edit_address(self, title, uuid):
        """编辑地址"""
        path = "backend/location/edit"
        data = {
            "title": title,
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def address_relocation(self, src_uuid, dst_uuid, rel, loc):
        """地址移动"""
        path = "backend/location/move"
        data = {
            "src_uuid": src_uuid,
            "dst_uuid": dst_uuid,
            "rel": rel,
            "loc": loc
        }
        return self.send("post", path, json=data)
