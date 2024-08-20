# -*- coding: utf-8 -*-
import base64
import json
import requests


class ApiRequest:
    # req_data = {
    #     "method": "get",
    #     "url": "http://120.79.84.33:9999/demo1.txt",
    #     "headers": None,
    #     "encoding": "base64"
    # }

    def send(self, data: dict):
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
        # 把加密过后的响应值发给第三方服务，让第三方去做解密然后返回
        elif data["encoding"] == "private":
            return requests.post("url", data=res.content)


api = ApiRequest()

req_data = {
    "method": "get",
    "url": "http://120.79.84.33:9999/demo1.txt",
    "headers": None,
    "encoding": "base64"
}


def test_send():
    print(api.send(req_data))
