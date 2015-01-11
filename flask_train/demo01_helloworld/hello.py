#coding:utf8
from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello_world():
	return "<h1>Hello flask world aaa</h1>"



if __name__=='__main__':
   #app.run()
   #app.run(host='0.0.0.0')
   app.run(host='0.0.0.0',port=80)