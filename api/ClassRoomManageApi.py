# -*- coding: utf-8 -*-
import json

from api.BaseApi import BaseApi


class ClassRoomManageApi(BaseApi):
    """"教室管理模块"""

    def idle_speaker(self, start_time, end_time, live_mode, room_type):
        """空闲主讲教室列表"""
        path = "backend/room/idle-speaker"
        data = {
            "start_time": start_time,
            "end_time": end_time,
            "live_mode": live_mode,
            "room_type": room_type
        }
        return self.send("get", path, params=data)

    def idle_listener(self, start_time, end_time, speaker_room_id, room_type):
        """空闲听课教室列表"""
        path = "backend/room/idle-listener"
        data = {
            "start_time": start_time,
            "end_time": end_time,
            "speaker_room_id": speaker_room_id,
            "room_type": room_type
        }
        return self.send("get", path, params=data)

    def add_classroom(self, title, location_uuid):
        """添加教室"""
        path = "backend/classroom/add"
        data = {
            "title": title,
            "location_uuid": location_uuid
        }
        return self.send("post", path, json=data)

    def classroom_list(self, page, size, status, location_uuid):
        """教室列表（带设备状态）"""
        path = "backend/classroom/lists"
        data = {
            "page": page,
            "size": size,
            "status": status,
            "location_uuid": location_uuid
        }
        return self.send("get", path, params=data)

    def del_classroom(self, uuid):
        """删除教室"""
        path = "backend/classroom/del"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def edit_classroom(self, uuid, title):
        """"编辑教室"""
        path = "backend/classroom/edit"
        data = {
            "uuid": uuid,
            "title": title
        }
        return self.send("post", path, json=data)

    def classroom_status(self):
        """教室状态统计"""
        path = "backend/classroom/status-count"
        return self.send("get", path)

    def classroom_list_select(self, page, size):
        """教室列表下拉框"""
        path = "backend/classroom/simple-list"
        data = {
            "page": page,
            "size": size
        }
        return self.send("get", path, params=data)

    def classroom_detail(self, uuid):
        """教室详情"""
        path = "backend/classroom/info"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def save_classroom_config_info(self, classroom_uuid, base_conf, cmd_conf, share_conf):
        """保存教室配置信息"""
        path = "backend/classroom/save-config"
        data = {
            "classroom_uuid": classroom_uuid,
            "base_conf": base_conf,
            "cmd_conf": cmd_conf,
            "share_conf": share_conf
        }
        return self.send("post", path, data=json.dumps(data))

    def get_classroom_config_info(self, classroom_uuid):
        """"获取教室配置信息"""
        path = "backend/classroom/config"
        data = {
            "classroom_uuid": classroom_uuid
        }
        return self.send("get", path, params=data)

    def classroom_add_device(self, classroom_uuid, line, cport, title):
        """教室添加设备"""
        path = "backend/classroom/device/add"
        data = {
            "classroom_uuid": classroom_uuid,
            "line": line,
            "cport": cport,
            "title": title
        }
        return self.send("post", path, json=data)

    def classroom_device_type(self):
        """获取教室设备类型以及限制数"""
        path = "backend/classroom/device/types"
        return self.send("get", path)

    def one_key_switch(self, status, is_all_classroom, classroom_uuid):
        """一键开关"""
        path = "backend/classroom/one-start"
        data = {
            "status": status,
            "is_all_classroom": is_all_classroom,
            "classroom_uuid": classroom_uuid
        }
        return self.send("post", path, json=data)

    def get_websocket_channel(self):
        """获取设备集控websocket频道号"""
        path = "backend/chatroom/channel/get"
        return self.send("get", path)
