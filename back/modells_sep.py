# -*- coding: utf-8 -*-
# @Time    : 19-1-2 下午4:57


from flask import Flask
from models import Article
from exts import db

app = Flask(__name__)
db.init_app(app)



db.create_all()

@app.route("/")
def index():
    return "index"

if __name__ == "__main__":
    app.run()
