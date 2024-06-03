# -*- coding: utf-8 -*-
from config.SassConfig import SassConfig

sass_config = SassConfig()


def test_base_url():
    """
    验证@property装饰器
    :return:
    """
    print(sass_config.base_url)
    print(sass_config.login_type)
    print(sass_config.username)
    print(sass_config.password)
