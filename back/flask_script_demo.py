# -*- coding: utf-8 -*-
# @Time    : 18-12-28 下午4:32


from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "index"

if __name__ == "__main__":
    app.run()
