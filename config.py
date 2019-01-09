# -*- coding: utf-8 -*-
# @Time    : 19-1-7 下午4:59

import os
DEBUG = True

SECRET_KEY = os.urandom(24)

#"mysql+pymysql://root:qq416200@127.0.0.1:3306/python"
DIALECT = "mysql"
DRIVER = "pymysql"
USERNAME = "root"
PASSWORD = "123456"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "db_demo3"
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
