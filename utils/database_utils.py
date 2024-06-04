# -*- coding: utf-8 -*-
import pymysql

from utils.log_utils import logger


class Database:
    """
    链接数据库之增删改查
    """

    @classmethod
    def query_db(cls, sql, database_info):
        """
        链接数据库，执行对应的sql语句，获得执行结果
        :param sql: 要执行的sql语句
        :param database_info: 数据库配置信息
        :return:
        """
        # 连接数据库
        conn = pymysql.Connect(**database_info)
        # 创建游标
        cursor = conn.cursor()
        logger.info(f"创建的游标为 {cursor}")
        logger.info(f"要执行的sql语句为 {sql}")
        # 执行sql语句
        cursor.execute(sql)
        # 获取查询结果
        datas = cursor.fetchall()
        logger.info(f"执行结果数据为 {datas}")
        # 关闭连接
        cursor.close()
        conn.close()
        return datas
