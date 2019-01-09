# -*- coding: utf-8 -*-
# @Time    : 18-12-28 下午4:34

from flask_script import Manager
from flask_script_demo import app
from db_scripts import DBmanager
manager = Manager(app)

#和数据库的操作我都放一起qq

@manager.command
def runserver():
    print("server is run")

manager.add_command("db",DBmanager)

if __name__ == "__main__":
    manager.run()

