# -*- coding: utf-8 -*-
from api.BaseApi import BaseApi


class UniversalApi(BaseApi):
    def upload_resource(self):
        path = "comm/upload"
        files = {
            "upload-file": ("dog.jpeg",
                            # open(r"E:\python_project\own_project\web_ui\sass_apiauto\files\dog.jpeg", "rb"),
                            open(r"files/dog.jpeg", "rb"),
                            "application/octet-stream",
                            )
        }
        return self.send("post", path, files=files)

