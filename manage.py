# -*- coding: utf-8 -*-
# @Time    : 19-1-7 下午5:32

from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from exts import db

from zlktqa import app

manager = Manager(app)

#使用migrate绑定app和db
migrate = Migrate(app,db)


#添加迁移脚本命令到manager中
manager.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manager.run()

