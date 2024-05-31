# -*- coding: utf-8 -*-
from genson import SchemaBuilder
from jsonschema.validators import validate
import json

from utils.log_utils import logger


class JsonSchemaUtils:
    @classmethod
    def generate_jsonschema(cls, obj):
        """
        生成 jsonschema 的数据
        :param obj: 待添加到模式中的对象
        :return:
        """
        # 创建 SchemaBuilder 类的实例
        builder = SchemaBuilder()
        # 将对象添加到构建器中
        builder.add_object(obj)
        # 获取构建器中累积的对象并转换为 JSONSchema
        return builder.to_schema()

    @classmethod
    def validate_schema(cls, data_obj, schema):
        """
        通过 schema 验证数据
        :param data_obj: 待验证的数据对象
        :param schema: 用于验证的 JSONSchema
        :return:
        """
        try:
            # 使用给定的 JSONSchema 验证数据对象
            validate(data_obj, schema=schema)
            # 验证通过返回 True
            return True
        except Exception as e:
            logger.info(f"结构体验证失败，失败原因是{e}")
            return False

    @classmethod
    def generate_jsonschema_by_file(cls, obj, file_path):
        """
        生成 schema 数据保存到文件中
        :param obj:
        :param file_path:
        :return:
        """
        jsonschema_data = cls.generate_jsonschema(obj)
        with open(file_path, "w") as f:
            json.dump(jsonschema_data, f)

    @classmethod
    def validate_schema_by_file(cls, data_obj, schema_file):
        """
        通过文件验证数据
        :param data_obj:
        :param schema_file:
        :return:
        """
        with open(schema_file) as f:
            schema_data = json.load(f)
        return cls.validate_schema(data_obj, schema_data)
