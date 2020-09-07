##sql injection=> 
##sql join=> done
##copy => Preference & key_bindings
##make new file => safe after coding



import sqlite3


# with sqlite3.connect("cars.db") as conn:
#     cursor = conn.cursor() 
#     cursor.execute("""CREATE TABLE orders
#               (make TEXT, model TEXT, order_date DATE)
#                """)

#     orders = [
#             ('Ford', 'Focus', '2014-01-22'),
#             ('Ford', 'Focus', '2014-01-23'),
#             ('Ford', 'Focus', '2014-01-24'),
#             ('Honda', 'Civic', '2014-01-25'),
#             ('Honda', 'Civic', '2014-01-26'),
#             ('Honda', 'Civic', '2014-01-27'),
#             ('Ford', 'Ranger', '2014-01-28'),
#             ('Ford', 'Ranger', '2014-01-22'),
#             ('Ford', 'Ranger', '2014-01-23'),
#             ('Honda', 'Accord', '2014-01-24'),
#             ('Honda', 'Accord', '2014-01-25'),
#             ('Honda', 'Accord', '2014-01-26'),
#             ('Ford', 'Avenger', '2014-01-27'),
#             ('Ford', 'Avenger', '2014-01-28'),
#             ('Ford', 'Avenger', '2014-01-22'),
#              ]

#     cursor.executemany("INSERT INTO orders VALUES(?, ?, ?)", orders)

#     cursor.execute("SELECT * FROM orders ORDER BY order_date ASC")

#     rows = cursor.fetchall()

#     for r in rows:
#         print(r[0], r[1], r[2])


import sqlite3

with sqlite3.connect("cars.db") as conn:
    cursor = conn.cursor()

    # retrieve data
    cursor.execute("""SELECT i.make, i.model,
            i.quantity, o.order_date FROM inventory i INNER JOIN orders o
            ON i.model = o.model""")

    rows = cursor.fetchall()

    for r in rows:
        print(r[0], r[1])
        print(r[2])
        print(r[3])
        print()