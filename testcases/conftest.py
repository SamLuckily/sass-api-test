# -*- coding: utf-8 -*-
# 读取yaml测试用例数据
from utils.read_utils import Utils


def get_data():
    path = Utils.get_root_path()
    file_path = f'{path}/data/use_cases.yaml'
    data = Utils.get_yaml_data(file_path)
    return data
