import sqlite3
import random

with sqlite3.connect("newnum.db") as conn:

  cursor=conn.cursor()

  cursor.execute("DROP TABLE if exists numbers")

  cursor.execute("CREATE TABLE numbers(num int)")

  for i in range(100):
    cursor.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),)) #important