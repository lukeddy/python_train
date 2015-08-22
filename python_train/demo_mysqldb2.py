# encoding:utf8
#TODO try to install mysql-python

import MySQLdb

try:
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="", db="imooc", charset="utf8")
    cur = conn.cursor()
    # conn.autocommit(False)
    # cur.execute('select * from tuser')
    try:
        sql_insert = "insert into tuser(usrname) values ('lucy')"
        sql_upate = "update tuser set usrname='jhon' where userid=1"
        sql_delete = "delete from tuser where userid=2"
        cur.execute(sql_insert)
        print cur.rowcount
        cur.execute(sql_upate)
        print cur.rowcount
        cur.execute(sql_delete)
        print cur
        conn.commit()
    except Exception as ex:
        print("Mysql Error cursor rollback %d: %s" % (ex.args[0], ex.args[1]))
        conn.rollback()
    finally:
        cur.close()
        conn.close()
except MySQLdb.Error as e:
    print("Mysql Error %d: %s" % (e.args[0], e.args[1]))