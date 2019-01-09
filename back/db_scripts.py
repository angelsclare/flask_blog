# -*- coding: utf-8 -*-
# @Time    : 18-12-28 下午4:50

from flask_script import Manager

DBmanager = Manager()

@DBmanager.command
def init():
    print("数据初始话完成")

@DBmanager.command
def migrate():
    print("数据迁移成功")


