# -*- coding: utf-8 -*-
# @Time    : 18-12-10 下午5:03

from flask import Flask,url_for,redirect,render_template
import config


app = Flask(__name__)
app.config.from_object(config)

@app.route("/")
def index():
    class Person(object):
        username = "杨dada"
        age = 18
    p = Person()

    context = {
        "username" : "样dada",
        "sex" : "男ddddd",
        "age" : 18,
        "person": p,
        "websites": {
            "baidu": "www.baidu.com",
            "google": "www.google.com"
        }

    }
    return render_template("index01.html",**context)

@app.route("/login")
def login():
    return "这是登录页面"

@app.route("/question/<is_login>")
def question(is_login):
    if is_login == "1":
        return "发表文章"
    else:
        return redirect(url_for("login"))


@app.route("/list/")
def my_list():
    return "list"
