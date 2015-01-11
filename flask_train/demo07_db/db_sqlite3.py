# coding:utf8
from flask import Flask, render_template, request
import sqlite3
import hashlib

app = Flask(__name__)


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        #insert into db
        conn = sqlite3.connect('my.db')
        cursor = conn.cursor()
        sql = 'insert into tusers(username,password) values(?,?)'
        cursor.execute(sql, (username, hashlib.new('md5', password).hexdigest()))
        conn.commit()
        cursor.close()
        conn.close()
        return '%s, %s' % (username, password)
    else:
        return render_template('regist.html')



if __name__ == '__main__':
    app.debug = True
    app.run()
