# -*- coding: utf-8 -*-
# @Time    : 18-12-21 下午4:51

from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route("/")
def index():
    return render_template("index21.html")

@app.route("/login/")
def login():
    return render_template("login21.html")


if __name__ == "__main__":
    app.run()
