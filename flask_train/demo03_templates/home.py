# coding:utf-8
from flask import Flask,render_template
import sys
reload(sys)
sys.setdefaultencoding('utf8')


app=Flask(__name__)

@app.route('/')
def hello_world():
	username="管理员"
	nav_list=[u'首页',u'经济',u'文化',u'政治',u'科技',u'娱乐']
	blog={'title':'标题一','content':'内容，内容，内容'}
	return render_template('home.html',username=username,nav_list=nav_list,blog=blog)


if __name__=='__main__':
	app.debug=True
	app.run()
