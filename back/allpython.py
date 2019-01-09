# -*- coding: utf-8 -*-
# @Time    : 18-12-17 下午4:20



from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<is_Login>/")
def index(is_Login):
    if is_Login == "1":
        user = {
            "username" : "样的",
            "age" : 17
        }
        return render_template("index.html",**user)
    else:
        render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
