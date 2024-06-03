# -*- coding: utf-8 -*-
import time
import jsonpath
import requests
from yaml import Token

from config.SassConfig import SassConfig
from utils.log_utils import logger
from utils.read_utils import Utils


class BaseApi:

    def access_token(self):
        """
        获取token
        问题：每次请求，都需要调用获取token,重复获取token。浪费资源
        解决方案：获取token之前添加判断，如果token存在于对象中的话则不获取token
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
        timestamp = jsonpath.jsonpath(r.json(), "$.timestamp")[0]
        return token, uuid, timestamp

    def config(self) -> SassConfig:
        """
        获取配置
        :return:
        """
        return SassConfig()

    def get_token_by_file(self, key):
        """
        从文件读取配置信息
        :param key:
        :return:
        """
        # 拿到存放token的文件路径
        path = Utils.get_root_path()
        file_path = f'{path}/data/token.yaml'
        try:
            token_data = Utils.get_yaml_data(file_path).get(key, {})
            time_stamp = token_data.get('time_stamp')
            access_token = token_data.get('access_token')
            # 获取时间差对 time_stamp 的检查，如果 time_stamp 不存在（即文件为空或 key 下没有 time_stamp），则默认其已过期
            time_step = time.time() - time_stamp if time_stamp else float('inf')
            # 判断token是否存在 以及时间戳是否过期
            if access_token is None or time_step >= 7200:
                new_token, new_uuid, new_timestamp = self.access_token()
                # 写入新数据
                new_token_data = {
                    'time_stamp': int(new_timestamp),
                    'access_token': new_token,
                    'uuid': new_uuid
                }
                Utils.add_yaml_data({key: new_token_data}, file_path)
                # 返回新的token
                return new_token
            else:
                # 返回已有token
                return access_token
        except Exception as e:
            logger.info(f"读取token文件失败或处理token时出错，错误信息为：{e}")
            return e

    def send(self, method, url, **kwargs):
        """
        请求方法
        :return:
        """
        request_url = self.config().base_url + url
        headers = {"Authorization": "Bearer " + self.get_token_by_file("contacts")}
        logger.info(f"发起的请求地址为===========>{request_url}")
        r = requests.request(method, request_url, headers=headers, **kwargs)
        logger.info(f"接口的响应信息为<==========={r.text}")
        # 如果所有的接口都可以进行json序列化的话，就直接return r.json()即可
        return r.json()
