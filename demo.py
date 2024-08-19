# # -*- coding: utf-8 -*-
# import time
# import jsonpath
# import requests
# from config.SassConfig import SassConfig
# from utils.log_utils import logger
# from utils.read_utils import Utils, utils_instance
#
#
# class BaseApi:
#
#     def access_token(self):
#         """
#         获取token
#         问题：每次请求，都需要调用获取token,重复获取token。浪费资源
#         解决方案：获取token之前添加判断，如果token存在于对象中的话则不获取token
#         :return:
#         """
#         headers = {"Content-Type": "application/json"}
#         data = {
#             "login_type": self.config().login_type,
#             "username": self.config().username,
#             "password": self.config().password
#         }
#         url = self.config().base_url + "v1/user/login"
#         r = requests.request("POST", url, headers=headers, json=data)
#         token = jsonpath.jsonpath(r.json(), "$..token")[0]
#         uuid = jsonpath.jsonpath(r.json(), "$..user_base.uuid")[0]
#         timestamp = jsonpath.jsonpath(r.json(), "$.timestamp")[0]
#         # path = utils_instance.get_root_path()
#         # Utils.add_yaml_data(f'{path}/data/token.yaml',
#         #                     {"access_token": token, "uuid": uuid, "timestamp": timestamp})
#         return token, uuid, timestamp
#
#     def get_token_by_file(self, key):
#         """
#         从文件读取配置信息
#         :param key:
#         :return:
#         """
#         # 拿到存放token的文件路径
#         path = utils_instance.get_root_path()
#         file_path = f'{path}/data/token.yaml'
#         try:
#             token_data = Utils.get_yaml_data(file_path).get(key, {})
#             time_stamp = token_data.get('time_stamp')
#             access_token = token_data.get('access_token')
#             # uuid = token_data.get('uuid')
#         except Exception as e:
#             logger.info(f"读取token文件失败，错误信息为：{e}")
#             return e
#         # 获取时间差
#         time_step = time.time() - time_stamp
#         # 判断token是否存在 以及时间戳是否过期
#         if access_token is None or time_step >= 7200:
#             new_token = self.access_token()
#             # 写入新数据
#             token_data.update({"time_stamp": int(time.time()), "access_token": new_token})
#             Utils.add_yaml_data({key: token_data}, file_path)
#             # 返回新的token
#             return new_token
#         else:
#             # 返回已有token
#             return access_token
#
#     def config(self) -> SassConfig:
#         """
#         获取配置
#         :return:
#         """
#         return SassConfig()
#
#     def send(self, method, url, **kwargs):
#         """
#         请求方法
#         :return:
#         """
#         request_url = self.config().base_url + url
#         # headers = {"Authorization": "Bearer " + self.access_token()[0]}
#         headers = {"Authorization": "Bearer " + self.get_token_by_file("contacts")}
#         logger.info(f"发起的请求地址为===========>{request_url}")
#         r = requests.request(method, request_url, headers=headers, **kwargs)
#         logger.info(f"接口的响应信息为<==========={r.text}")
#         # 如果所有的接口都可以进行json序列化的话，就直接return r.json()即可
#         return r.json()

# original_string = "1, 2, 3"
# result_list = original_string.split(', ')
# print(result_list)
# result_list_cleaned = [item.strip() for item in result_list]
# print(result_list_cleaned)
# from datetime import datetime
#
#
# def deact(input_time_str):
#     # 将输入的时间字符串转换为datetime对象
#     try:
#         input_time = datetime.strptime(input_time_str, '%Y-%m-%d %H:%M:%S')
#     except ValueError:
#         print("输入的时间格式不正确，请使用'YYYY-MM-DD HH:MM:SS'格式")
#         return
#
#         # 获取当前时间
#     current_time = datetime.now()
#
#     # 比较时间
#     if input_time > current_time:
#         print("deact")
#     else:
#         print("输入的时间不大于当前时间")

# 示例用法


# deact("2024-10-01 12:00:00")  # 假设当前时间小于这个值
# 如果需要测试当前时间或未来某个时间，请确保你的系统时间设置正确

# import requests
# import base64
# import json
#
#
# def test_encode():
#     url = "http://120.79.84.33:9999/demo1.txt"
#     r = requests.get(url=url)
#     # res = base64.b64encode(r.content)
#     res = json.loads(base64.b64decode(r.content))
#     print(res)

# group_uuids = ["125e8169431c8bda95e3894c2d1ca677", "dc108a00e29b633edbd932a4ee8a5df4"]
# for group_uuid in group_uuids:
#     print(group_uuid)
import json

# speaker_rooms = [{
#     "org_id": 12,
#     "room_id": 23,
#     "room_uuid": 3443,
#     "room_name": 56889,
#     "title": 4344,
#     "mac": 21223222,
#     "action": 23233
# }, {
#     "org_id": 12,
#     "room_id": 23,
#     "room_uuid": 3443,
#     "room_name": 56889,
#     "title": 4344,
#     "mac": 21223222,
#     "action": 23233
# }
# ]
# speaker_rooms_json = json.dumps(speaker_rooms)
# print(speaker_rooms_json)
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# 将Python字典序列化为JSON格式的字符串
# print(f"我是python字典：{data}")
# json_str = json.dumps(data)
# print(f"我是json格式字符串 + {json_str}")

# json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
# python_obj = json.loads(json_str)
# print(python_obj)
# 将数据写入JSON文件
# with open("data.json", "w") as file:
#     json.dump(data, file)
#
# with open("data.json", "r") as files:
#     data = json.load(files)
# print(data)

# json_str = '{"name": "Alice", "age": 30, "city": "New York"}'
#
# # 将JSON字符串解码为Python对象
# Python_obj = json.loads(json_str)
# print(Python_obj)
# with open("data.json", "r") as file:
#     data = json.load(file)
# print(data)
