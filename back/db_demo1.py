# -*- coding: utf-8 -*-
# @Time    : 18-12-24 下午3:59
import io
from flask import Flask
import config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

db.create_all()

@app.route("/")
def index():
    return "index"

if __name__ == "__main__":
    app.run()


