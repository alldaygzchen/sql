import sqlite3

with sqlite3.connect("new.db") as conn:

  cursor=conn.cursor()

  sql={'average':"SELECT avg(population) FROM population",
  'maximum':"SELECT max(population) FROM population",
  'minimum':"SELECT min(population) FROM population",
  'sum':"SELECT sum(population) FROM population",
  'count':"SELECT count(city) FROM population"}

  #cursor.execute("SELECT * from population")
  #result=cursor.fetchall()
  #print(result)


  for keys, values in sql.items():

    cursor.execute(values)

    result=cursor.fetchall()

    print(keys + ":",result[0][0])