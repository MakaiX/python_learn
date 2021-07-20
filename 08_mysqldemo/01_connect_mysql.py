from pymysql import *

connection = connect(host='localhost', port=3306, database='ods', user='root', password='mark1005', charset='utf8')

cursor = connection.cursor()

for i in range(100000):
    cursor.execute("insert into test_index values ('哈-%d')" % i)
connection.commit()
