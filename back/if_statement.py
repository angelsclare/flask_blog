# -*- coding: utf-8 -*-
# @Time    : 18-12-17 下午3:44

from flask import Flask,render_template

app = Flask(__name__)

# @app.route("/")
# def index():
#     user = {
#         "username": "样的",
#         "age": 17
#     }
#     websites = ["baidu.com","goolge.com"]
#     return render_template("index.html",user=user,websites=websites)


@app.route("/")
def index():
    books = [
        {
            "name": "西游记",
            "author": "五成恩",
            "price": 100
        },
        {
            "name": "红楼梦",
            "author": "曹雪芹",
            "price": 200
        },
        {
            "name": "三国演义",
            "author": "罗观众",
            "price": 120
        },
        {
            "name": "说服钻",
            "author": "使乃按",
            "price": 130
        }
    ]


    return render_template("index.html",books=books)

if __name__ == "__main__":
    app.run(debug=True)


