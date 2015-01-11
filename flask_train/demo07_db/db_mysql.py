# coding:utf8
from flask import Flask, render_template, request
# import MySQLdb


app = Flask(__name__)


@app.route('/regist_mysql/', methods=['GET', 'POST'])
def regist():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        #TODO fix the db error, insert into db,
        # conn = MySQLdb.connect(host='localhost', user='root', passwd='')
        # conn.select_db('flaskdb');
        # cursor = conn.cursor()
        # cursor.execute("select * from tusers")
        # data = cursor.fetchone()
        # cursor.close()
        # conn.close()
        # print data[1]
        return '%s, %s' % (username, password)
    else:
        return render_template('regist.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
