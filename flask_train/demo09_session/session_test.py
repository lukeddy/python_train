# coding:utf8
from flask import Flask, render_template, request, make_response, redirect, session
app = Flask(__name__)
app.secret_key = '\xc4\x03w\x05d~7\xd9\xd9\xc0K\xe1\xf4M[\xfbA(\x9a\x88\x0e\xa7\xce\x8d'
user_list = ['alien', 'max', 'aw']


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if username in user_list:
            session['username'] = username
            return redirect('/index/')
        else:
            return redirect('/login/')
    else:
        return render_template('login.html')


@app.route('/index/')
def index():
    username = session.get('username')
    if username:
        return render_template('index.html', username=username)
    else:
        return redirect('login')


if __name__ == '__main__':
    app.debug = True
    app.run()
