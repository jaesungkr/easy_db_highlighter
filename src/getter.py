'''
CREATE USER 'krjaesung'@'localhost' IDENTIFIED BY '1234';
grant all privileges on *.* to 'krjaesung'@'localhost';
'''

import pymysql


conn = pymysql.connect(host='localhost', user='krjaesung', password='1234', db = 'employees', charset='utf8')

cur = conn.cursor()

query = """SELECT COUNT(*) 
           FROM employees.salaries;"""

cur.execute(query)
conn.commit()
result = cur.fetchall()
print(result)
conn.close()