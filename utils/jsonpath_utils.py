# -*- coding: utf-8 -*-
import jsonpath

from utils.log_utils import logger


class JsonPathUtils:
    @classmethod
    def get(cls, obj, expr):
        res = jsonpath.jsonpath(obj, expr)
        logger.info(f"通过jsonpath获取到的数据为{res}")
        return res
