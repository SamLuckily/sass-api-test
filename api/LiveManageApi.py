# -*- coding: utf-8 -*-
import json

from api.BaseApi import BaseApi


class LiveManageApi(BaseApi):
    """直播管理"""

    def live_list(self, page, size):
        """直播列表"""
        path = "backend/v2/live/list"
        data = {
            "page": page,
            "size": size
        }
        return self.send("get", path, params=data)

    def live_create(self, title, start_time, end_time, org_id, room_id, room_uuid, room_name, titles, mac, action,
                    playback_mode, interactive_mode, live_mode,
                    speaker_room_type, listener_room_type, push_source_type, speaker_uuid, resource_uuid):
        """创建直播"""
        path = "backend/v2/live/create"
        # 构建 speaker_rooms 字段的值为 JSON 字符串
        speaker_rooms = [{
            "org_id": org_id,
            "room_id": room_id,
            "room_uuid": room_uuid,
            "room_name": room_name,
            "title": titles,
            "mac": mac,
            "action": action
        }]
        speaker_rooms_json = json.dumps(speaker_rooms)
        data = {
            "title": title,
            "start_time": start_time,
            "end_time": end_time,
            "speaker_rooms": speaker_rooms_json,
            "playback_mode": playback_mode,
            "interactive_mode": interactive_mode,
            "live_mode": live_mode,
            "speaker_room_type": speaker_room_type,
            "listener_room_type": listener_room_type,
            "push_source_type": push_source_type,
            "speaker_uuid": speaker_uuid,
            "resource_uuid": resource_uuid
        }
        return self.send("post", path, json=data)

    def file_upload(self, md5, file_name, type):
        """文件md5查重"""
        path = "comm/upload/checkMd5"
        data = {
            "md5": md5,
            "file_name": file_name,
            "type": type
        }
        return self.send_md5("post", path, json=data)

    def live_detail(self, uuid):
        """直播详情"""
        path = "backend/v2/live/detail"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def live_del(self, uuid):
        """直播删除"""
        path = "backend/v2/live/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def update_live(self, uuid, title, start_time, end_time, live_uuid, org_id, room_id, room_uuid, room_name, titles,
                    mac, action,
                    playback_mode, interactive_mode, live_mode,
                    speaker_room_type, listener_room_type, push_source_type, speaker_uuid, resource_uuid):
        """直播编辑"""
        path = "backend/v2/live/update"
        # 构建 speaker_rooms 字段的值为 JSON 字符串
        speaker_rooms = [{
            "live_uuid": live_uuid,
            "org_id": org_id,
            "room_id": room_id,
            "room_uuid": room_uuid,
            "room_name": room_name,
            "title": titles,
            "mac": mac,
            "action": action
        }]
        speaker_rooms_json = json.dumps(speaker_rooms)
        data = {
            "uuid": uuid,
            "title": title,
            "start_time": start_time,
            "end_time": end_time,
            "speaker_rooms": speaker_rooms_json,
            "playback_mode": playback_mode,
            "interactive_mode": interactive_mode,
            "live_mode": live_mode,
            "speaker_room_type": speaker_room_type,
            "listener_room_type": listener_room_type,
            "push_source_type": push_source_type,
            "speaker_uuid": speaker_uuid,
            "resource_uuid": resource_uuid
        }
        return self.send("post", path, json=data)

    def create_image_text_live(self, uuid, enable_graphic, introduce, images):
        """直播图文创建"""
        # if isinstance(images, str):  # 如果传入的是字符串类型，则将其转换为包含单个图片链接的列表
        #     images = [images]
        path = "backend/v2/live/graphic/create"
        data = {
            "uuid": uuid,
            "enable_graphic": enable_graphic,
            "introduce": introduce,
            "images": [images]
        }
        return self.send("post", path, json=data)

    def del_image_text_live(self, uuid):
        """直播图文删除"""
        path = "backend/v2/live/graphic/delete"
        data = {
            "uuid": uuid
        }
        return self.send("post", path, json=data)

    def list_name(self):
        """"直播名称列表"""
        path = "backend/v2/live/title-list"
        return self.send("get", path)

    def get_share_link(self, uuid):
        """获取分享连接"""
        path = "backend/live/share"
        data = {
            "uuid": uuid
        }
        return self.send("get", path, params=data)

    def quick_edit(self, uuid, type, value):
        """快速编辑"""
        path = "backend/live/fast-update"
        data = {
            "uuid": uuid,
            "type": type,
            "value": value
        }
        return self.send("post", path, json=data)
