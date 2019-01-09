# -*- coding: utf-8 -*-
# @Time    : 18-12-25 上午11:16

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

# article表:
# create table article (
#     id int property key autoincrement,
#     titke varchar(100) not null,
#     content text not null,
# )

#数据库操作命令
# use python;
# show tables;
# desc article;

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)

db.create_all()

@app.route("/")
def index():
    #增加数据
    # article1 = Article(title="aaa",content="bbb")
    # db.session.add(article1)
    # #事务
    # db.session.commit()
    #查
    #select * from artice whele title="aaa"
    # article1 = Article.query.filter(Article.title == "aaa").first()
    # # article1 = result[0]
    # # print(article1.title)
    # # print(article1.content)
    # print("title:%s" % article1.title)
    # print("content:%s" % article1.content)
    # return "index"
    #改
    # article1 = Article.query.filter(Article.title == "aaa").first()
    # article1.title = "new title"
    # db.session.commit()
    #删
    #查找需要删除的数据
    #做事务提交
    article1 = Article.query.filter(Article.content == "bbb").first()
    db.session.delete(article1)
    db.session.commit()
    return "index"

if __name__ == "__main__":
    app.run()
