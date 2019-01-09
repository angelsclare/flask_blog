# -*- coding: utf-8 -*-
# @Time    : 18-12-18 下午4:34
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    comments = [
        {
        "user" : "dada",
        "contnet": "xxxx"
        },
        {
            "user": "dada",
            "contnet": "dada"
        }

    ]
    return render_template("index02.html",comments=comments)

if __name__ == "__main__":
    app.run(debug=True)
