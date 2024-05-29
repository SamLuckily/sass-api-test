# -*- coding: utf-8 -*-
import jsonpath
import requests
from config.SassConfig import SassConfig
from utils.log_util import logger


class BaseApi:

    def access_token(self):
        """
        获取token
        :return:
        """
        headers = {"Content-Type": "application/json"}
        data = {
            "login_type": self.config().login_type,
            "username": self.config().username,
            "password": self.config().password
        }
        url = self.config().base_url + "v1/user/login"
        r = requests.request("POST", url, headers=headers, json=data)
        token = jsonpath.jsonpath(r.json(), "$..token")[0]
        uuid = jsonpath.jsonpath(r.json(), "$..user_base.uuid")[0]
        return token, uuid

    def config(self) -> SassConfig:
        """
        获取配置
        :return:
        """
        return SassConfig()

    def send(self, method, url, **kwargs):
        """
        请求方法
        :return:
        """
        request_url = self.config().base_url + url
        headers = {"Authorization": "Bearer " + self.access_token()[0]}
        logger.info(f"发起的请求地址为===========>{request_url}")
        r = requests.request(method, request_url, headers=headers, **kwargs)
        logger.info(f"接口的响应信息为<==========={r.text}")
        # 如果所有的接口都可以进行json序列化的话，就直接return r.json()即可
        return r.json()
