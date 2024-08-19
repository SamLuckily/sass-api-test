# -*- coding: utf-8 -*-
import os
import yaml

from utils.read_utils import Utils


class SassConfig:
    def __init__(self):
        # 从环境变量去获取切换的环境信息
        file_path = os.getenv("env", default="test")
        # 拼接文件名
        path = Utils.get_root_path()
        file_path = f"{path}/config/" + file_path + ".yaml"
        # 读取对应的文件
        with open(file_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    @property  # 方法---》属性：通过添加@property装饰器即可实现
    def base_url(self):
        # return self.config.get("base_url")
        return self.config["base_url"]

    @property  # 方法---》属性：通过添加@property装饰器即可实现
    def upload_url(self):
        # return self.config.get("base_url")
        return self.config["upload_url"]

    @property
    def login_type(self):
        return self.config["login_type"]

    @property
    def username(self):
        return self.config["username"]

    @property
    def password(self):
        return self.config["password"]
