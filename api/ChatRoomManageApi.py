# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class ChatRoomManageApi(BaseApi):
    """聊天室管理模块"""

    def get_all_members(self, channel):
        """获取全部成员"""
        path = "backend/chatroom/members"
        data = {
            "channel": channel
        }
        return self.send("get", path, params=data)
