import sqlite3

with sqlite3.connect('new.db') as conn:
  
  cursor=conn.cursor()

  cursor.execute("UPDATE population SET population=900000 WHERE city='New York City';")

  cursor.execute("DELETE FROM population WHERE city='Boston';")

  cursor.execute("SELECT * FROM population;")

  rows=cursor.fetchall()

  for r in rows:

    print(r[0],r[1],r[2])

