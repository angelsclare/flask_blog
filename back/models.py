# -*- coding: utf-8 -*-
# @Time    : 19-1-2 下午4:46
from exts import db

class Article(db.Model):
    __tablename = "article"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
