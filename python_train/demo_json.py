#encoding:utf-8
import json

def testPython():
	d={}
	d['dic']={'key1':'value1','key2':'value2'}
	d['id']=128
	d['name']='abc'
	d['tags']=('baidu','google','360','bing')
	d['bo']=True
	d['n']=None
	with open('test.json','w') as f:
	      #json.dump(d,f)
	      json.dump(d,f,indent=2)


testPython()	      
