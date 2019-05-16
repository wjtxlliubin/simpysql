#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .Connection import connection
from .Builder import Builder
import time


class DBModel():

    __connection__ = connection

    __create_time__ = None              # 插入时间字段

    __update_time__ = None              # 更新时间字段

    # 获取创建时间字段
    def create_time_column(self):
        return self.__create_time__

    # 获取更新时间字段
    def update_time_column(self):
        return self.__update_time__

    # 获取当前时间戳
    def fresh_timestamp(self):
        return int(time.time())

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, '__database__'):
            connection.set_config(cls.__basepath__, cls.__database__)
        else:
            connection.set_config(cls.__basepath__)
        return Builder(super(DBModel, cls).__new__(cls, *args, **kwargs))
