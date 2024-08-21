# -*- coding: utf-8 -*-
import json

from api.BaseApi import BaseApi


class GlobalTimingApi(BaseApi):
    """全局定时模块"""

    def edit_time_task(self, is_global_timing, on_type, on_status, on_device, on_timer, lession_on_timer, on_week,
                       off_status, off_device, off_timer, off_week):
        """编辑定时任务"""
        path = "backend/scheduled-task/edit"
        data = {
            "is_global_timing": is_global_timing,
            "on_type": on_type,
            "on_status": on_status,
            "on_device": on_device,
            "on_timer": on_timer,
            "lession_on_timer": lession_on_timer,
            "on_week": on_week,
            "off_status": off_status,
            "off_device": off_device,
            "off_timer": off_timer,
            "off_week": off_week
        }
        return self.send("post", path, json=data)

    def get_time_task(self):
        """获取定时任务信息"""
        path = "backend/scheduled-task/get"
        return self.send("get", path)
