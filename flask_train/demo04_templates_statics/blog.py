#coding:utf8
from flask import Flask,render_template,url_for


app=Flask(__name__)

@app.route('/')
def hello_world():
	username="xiaoqiang"
    #img=url_for('static', 'images/qukuailian.jpg' )
	return render_template('blog.html', username=username)


if __name__=='__main__':
	app.debug=True
	app.run()
