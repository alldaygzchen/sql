import csv
import sqlite3

with sqlite3.connect("new.db") as conn:
  
  cursor=conn.cursor()
  employees=csv.reader(open('employees.csv','rU'))
  
  cursor.execute("DROP TABLE IF EXISTS People;")


  cursor.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT);")

  cursor.executemany("INSERT INTO employees(firstname,lastname) values(?,?);",employees)

  cursor.execute("SELECT * from employees;")

  rows=cursor.fetchall()

  for r in rows:
    print(r)
