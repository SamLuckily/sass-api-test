# -*- coding: utf-8 -*-
import datetime


class TimeStampUtils:
    @classmethod
    def get_current_timestamp(cls):
        """获取当前时间戳"""
        current_time = datetime.datetime.now()
        # 往后推3秒
        future_time_second = current_time + datetime.timedelta(minutes=1)
        # 往后推1小时
        future_time_hour = current_time + datetime.timedelta(hours=1)
        # 将future_time转换为时间戳
        future_timestamp_second = int(future_time_second.timestamp())
        future_timestamp_hour = int(future_time_hour.timestamp())

        return future_timestamp_second, future_timestamp_hour

# print(TimeStampUtils.get_current_timestamp()[0])
# print(TimeStampUtils.get_current_timestamp()[1])
