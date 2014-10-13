# Homework p76

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT inventory.Make, inventory.Model,
	inventory.Quantity, orders.order_date
	FROM inventory INNER JOIN orders ON inventory.Model = orders.model""")

    rows = c.fetchall()

    for r in rows:
        print r[0], r[1]
        print r[2]
        print r[3]
        print

