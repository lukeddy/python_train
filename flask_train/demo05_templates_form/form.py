#coding:utf8
from flask import Flask,render_template,request


app=Flask(__name__)


@app.route('/regist/',methods=['GET','POST'])
def regist():
	if request.method =='POST':

		return "user %s regist OK"% request.form['username']
	     
	else:
		return render_template('form.html')


if __name__=='__main__':
	app.debug=True
	app.run()
