import sqlite3

with sqlite3.connect('cars.db') as conn:

  cursor=conn.cursor()

  sql = {'Focus count'    : "SELECT count(make) FROM orders WHERE model = 'Focus'",
        'Civic count'   : "SELECT count(make) FROM orders WHERE model = 'Civic'",
        'Ranger count'  : "SELECT count(make) FROM orders WHERE model = 'Ranger'",
        'Accord count'  : "SELECT count(make) FROM orders WHERE model = 'Accord'",
        'Avenger count' : "SELECT count(make) FROM orders WHERE model = 'Avenger'",}


  #cursor.execute("SELECT * FROM orders WHERE model='Focus'")
  
  #result=cursor.fetchall()

  #print(result)

  




  # for keys, values in sql.items():

  #   cursor.execute(values)

  #   result=cursor.fetchone()

  #   print(keys + ":",result[0])