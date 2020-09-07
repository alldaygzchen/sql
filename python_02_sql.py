import sqlite3

conn=sqlite3.connect('new.db')
cursor=conn.cursor()

cursor.execute("INSERT INTO population VALUES('New York City',\
  'NY',8400000)")

cursor.execute("INSERT INTO population VALUES('San Fransisco',\
  'CA',800000)")

conn.commit()
conn.close()

print('Nice')

with sqlite3.connect('new.db') as conn:
  cursor=conn.cursor()
  cursor.execute("INSERT INTO population VALUES('Taipei City',\
  'TP',8400)")

print('Nice')


with sqlite3.connect('new.db') as conn:
  cursor=conn.cursor()

  cities=[

  ('Boston', 'MA', 600000),
  ('Chicago', 'IL', 2700000),
  ('Houston', 'TX', 2100000),
  ('Phoenix', 'AZ', 1500000)
  ]

  cursor.executemany("INSERT INTO population VALUES(?,?,?)",cities)
