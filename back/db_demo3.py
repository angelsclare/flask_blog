# -*- coding: utf-8 -*-
# @Time    : 18-12-26 下午2:44

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

#用户表
# create table users(
#     id int primary key autoincrement,
#     username varchar(100) not null
# )
#
# #文章表
# create table article(
#     id int primary key autoincrement,
#     title vatchar(100) not null,
#     content text not null,
#     author_id int,
#     foreign key `author_id` references `users.id`
# )

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100),nullable=False)
    #password = db.Column(db.String(100), nullable=False)

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))      #引用id

    aaa = db.relationship("User",backref=db.backkref("article"))

db.create_all()

"""
use db_demo3;
show create table user;


"""


@app.route("/")
def index():
    #添加一篇文章,文章依赖用户,所限先添加用户
    # user1 =User(username="yangxiao")
    # db.session.add(user1)
    # db.session.commit()

    # article = Article(title="aaa",content="bbb",author_id=1)
    # db.session.add(article)
    # db.session.commit()

    #我要找到文章标题为aaa的作者
    # article = Article.query.filter(Article.title == "aaa").first()
    # author_id = article.author_id
    # user = User.query.filter(User.id == author_id).first()
    # print(user.username)


    return "index"

if __name__ == "__main__":
    app.run()
