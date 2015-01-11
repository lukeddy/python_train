# coding:utf8
from flask import Flask, render_template, request
import os


app = Flask(__name__)

upload_path = os.path.join(os.getcwd(), 'static')


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        username = request.form['username']
        uploadfile = request.files['file']
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        uploadfile.save(os.path.join(upload_path, uploadfile.filename))
        return 'user %s regist OK, picture is: <br/><img src="/static/%s"/> ' % (username, uploadfile.filename)

    else:
        return render_template('form.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
