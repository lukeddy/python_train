#encoding:utf8
#TODO try to install mysql-python

import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='test',port=3306)
    cur=conn.cursor()
    cur.execute('select * from tusers')
    cur.close()
    conn.close()
except MySQLdb.Error as e:
     print("Mysql Error %d: %s" % (e.args[0], e.args[1]))