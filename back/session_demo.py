# -*- coding: utf-8 -*-
# @Time    : 19-1-4 下午5:06

from flask import Flask,session
import os
app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

@app.route("/")
def index():
    session["username"] = "dada"
    return "index"

@app.route("/get/")
def get():
    return session.get("username")

@app.route("/delsion/")
def delsion():
    print(session.get("username"))
    session.pop("username")
    #session.clear("username")
    print(session.get("username"))
    return "delsion"

if __name__ == "__main__":
    app.run()
