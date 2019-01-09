# -*- coding: utf-8 -*-
# @Time    : 19-1-3 下午4:50

from flask import Flask
app = Flask(__name__)




@app.route("/")
def index():
    return "index"

if __name__ == "__main__":
    app.run()
