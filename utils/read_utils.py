# -*- coding: utf-8 -*-
import os
import yaml


class Utils:

    @classmethod
    def get_root_path(cls):
        """
        获取项目的绝对路径
        :return:
        """
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return path

    @classmethod
    def get_yaml_data(cls, file_path):
        """
        读取yaml文件
        :param file_path:
        :return:
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    @classmethod
    def add_yaml_data(cls, data, file_path):
        """
        写入yaml文件
        :param file_path:
        :param data:
        :return:
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f)
