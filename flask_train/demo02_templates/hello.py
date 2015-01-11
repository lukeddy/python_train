# coding:utf8
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    username = "xiaoqiang"
    return render_template('hello.html', username=username)


if __name__ == '__main__':
    app.debug = True
    app.run()
