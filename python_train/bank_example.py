# encoding:utf8
# TODO 模拟转账操作

import MySQLdb
import sys


#转账封装类
class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    #转账方法
    def transfer(self, source_acctid, target_acctid, money):
        self.check_acct_available(source_acctid)
        self.check_acct_available(target_acctid)
        self.has_enough_money(source_acctid, money)
        self.reduce_money(source_acctid, money)
        self.add_money(target_acctid, money)
        self.conn.commit()

    #检查账户是否存在
    def check_acct_available(self, acctid):
        try:
            cursor = conn.cursor()
            sql = "select * from account where acctid=%s" % acctid
            cursor.execute(sql)
            print "帐号存在:"+sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("帐号%s不存在" % acctid)
        finally:
            cursor.close()

    #检查账户是否有足够的钱
    def has_enough_money(self, acctid, money):
        try:
            cursor = conn.cursor()
            sql = "select * from account where acctid=%s and money>%s" % (acctid, money)
            cursor.execute(sql)
            print "帐号有足够的钱，可以转账:"+sql
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("帐号%s没有足够的钱，不能转账" % acctid)
        finally:
            cursor.close()

    #帐号减款
    def reduce_money(self, acctid, money):
        try:
            cursor = conn.cursor()
            sql = "update account set money=money-%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print "reduce_money："+sql
            if cursor.rowcount != 1:
                raise Exception("帐号%s减款失败" % acctid)
        finally:
            cursor.close()

    #帐号加款
    def add_money(self, acctid, money):
        try:
            cursor = conn.cursor()
            sql = "update account set money=money+%s where acctid=%s" % (money, acctid)
            cursor.execute(sql)
            print "add_money："+sql
            if cursor.rowcount != 1:
                raise Exception("帐号%s加款失败" % acctid)
        finally:
            cursor.close()



#主方法
if __name__ == "__main__":
    source_acctid = sys.argv[1]
    target_acctid = sys.argv[2]
    money = sys.argv[3]

    conn = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="", db="imooc", charset="utf8")
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid, target_acctid, money)

    except Exception as e:
        print "转账出现问题" + str(e)