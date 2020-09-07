import sqlite3

with sqlite3.connect('cars.db') as conn:

  cursor=conn.cursor()


  cursor.execute("DROP TABLE if EXISTS inventory")
  cursor.execute("CREATE TABLE inventory(MAKE TEXT, MODEL TEXT,Quantity INT);")

  values=[

  ('Ford', 'Focus', 10),
  ('Honda', 'Civic', 11),
  ('Ford', 'Ranger', 12),
  ('Honda', 'Accord', 13),
  ('Ford','Avenger',14)

  ]

  cursor.executemany("INSERT INTO inventory VALUES(?,?,?);",values)

  cursor.execute("UPDATE inventory SET quantity=15 WHERE model='Focus';")
  cursor.execute("UPDATE inventory SET quantity=16 WHERE model='Civic';")

  cursor.execute("SELECT * FROM inventory WHERE make='Ford';")

  rows=cursor.fetchall()

  for r in rows:

    print(r[0],r[1],r[2])

