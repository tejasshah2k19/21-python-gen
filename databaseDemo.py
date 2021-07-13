#mysql driver
#mysql connector

#pip install mysql-connector-python

import mysql.connector as con
#host --> your db url where is database? local computer--current pc --> localhost
#amazon --> amazon ip -> cloud url -->
mydb = con.connect(host="localhost",user="root",password="root",database="21pythonr")
print("Enter courseName")
courseName = input()
print("Enter price")
price = int(input())
#cursor --> db memory [1-> implicit 2->explicit ]
cur = mydb.cursor()
cur.execute("insert into course (courseName,price) values (%s,%s)",(courseName,price))
mydb.commit() # save
mydb.close() #close





