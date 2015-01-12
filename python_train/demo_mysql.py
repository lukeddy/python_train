#encoding:utf8
#install mysql connector for python http://dev.mysql.com/downloads/connector/python/
from datetime import date, datetime, timedelta
import mysql.connector

DB_NAME="ptestdb"

# ================Create DB==========================
# cnx = mysql.connector.connect(user='root')
# cursor = cnx.cursor()
# try:
#     cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
# except mysql.connector.Error as err:
#         print("Failed creating database: {}".format(err))
#         exit(1)
# print("Create db %s successfully"%(DB_NAME))

# cursor.close()
# cnx.close()




# ===============Create Table==========================
# cnx = mysql.connector.connect(user='root', database=DB_NAME)
# cursor = cnx.cursor()

# TABLES = {}
# TABLES['tusers'] = (
#     "CREATE TABLE `tusers` ("
#     "  `id` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `created_date` date NOT NULL,"
#     "  `username` varchar(14) NOT NULL,"
#     "  `password` varchar(16) NOT NULL,"
#     "  PRIMARY KEY (`id`)"
#     ") ENGINE=InnoDB")

# TABLES['departments'] = (
#     "CREATE TABLE `departments` ("
#     "  `dept_no` char(4) NOT NULL,"
#     "  `dept_name` varchar(40) NOT NULL,"
#     "  PRIMARY KEY (`dept_no`), UNIQUE KEY `dept_name` (`dept_name`)"
#     ") ENGINE=InnoDB")


# for name, ddl in TABLES.items():
#     try:
#         print("Creating table {}: ".format(name), end='')
#         cursor.execute(ddl)
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
#             print("already exists.")
#         else:
#             print(err.msg)
#     else:
#         print("OK")

# cursor.close()
# cnx.close()



# =================Insert data to DB=================
cnx = mysql.connector.connect(user='root', database=DB_NAME)
cursor = cnx.cursor()
data_user={
	'username':'Lucy',
	'password':'ssfsfs44242',
	'created_date':datetime.now().date()
}

insertSQL=("insert into tusers(username,password,created_date) values(%(username)s,%(password)s,%(created_date)s)")
cursor.execute(insertSQL,data_user)
cnx.commit()

print('insert successfully')
cursor.close()
cnx.close()



# =================Query data from DB================
#cnx = mysql.connector.connect(user='root', password='',host='127.0.0.1',database='test')
cnx = mysql.connector.connect(user='root', database=DB_NAME)
cursor = cnx.cursor()
query = ("SELECT username, password, created_date FROM tusers")

hire_start = date(1999, 1, 1)
hire_end = date(2015, 12, 31)

print(hire_start,hire_end)

cursor.execute(query)

for (username, password, created_date) in cursor:
  print(username, password, created_date)

cursor.close()
cnx.close()


# ================Delete data from DB=================
cnx = mysql.connector.connect(user='root', database=DB_NAME)
cursor = cnx.cursor()   

delSQL = "delete from tusers where username = %s"     
param =("wangwu")      
n = cursor.execute(delSQL,(param,)) 

cnx.commit()
print("successfully delete data:",n)    

cursor.close()  
cnx.close() 