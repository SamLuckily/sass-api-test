# -*- coding: utf-8 -*-
import hashlib


class Md5:
    """文件二进制md5值"""

    @classmethod
    def file_md5(cls, filename):
        hash_md5 = hashlib.md5()
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    # 上传资源: 这个方法目前先不用后期有删除资源后根据业务统一测试目前已经调通
    # md5_value = Md5.file_md5("E:\\python_project\\own_project\\web_ui\\sass_apiauto\\files\\视频.mp4")
    # print(md5_value)
    # self.live_manage.file_upload(md5_value, "视频.mp4", 6)
