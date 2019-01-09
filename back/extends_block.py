# -*- coding: utf-8 -*-
# @Time    : 18-12-20 下午5:15
from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

class Person():
    name = ""
    age = 0

class Student(Person):
    pass

@app.route("/")
def index():
    return render_template("index16.html")

@app.route("/login/")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run()

