import sqlite3
# 
#with sqlite3.connect("new.db") as conn:
#   cursor = conn.cursor()
# # use a for loop to iterate through the database, printing the results line by
# #line
#   for row in cursor.execute("SELECT firstname, lastname from employees"):
#     #print(row)
#     print(row[0],row[1])

# conn.commit()
# conn.close()

import sqlite3
with sqlite3.connect("new.db") as conn:
  cursor = conn.cursor()
  cursor.execute("SELECT firstname, lastname from employees")
  # fetchall() retrieves all records from the query
  rows = cursor.fetchall()
  # output the rows to the screen, row by row
  for r in rows:
    print(r[0], r[1])

conn.commit()
conn.close()