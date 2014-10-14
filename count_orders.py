# Homework p78

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()
    c.execute("""SELECT count(orders.model) FROM orders""")

result = c.fetchone()
print "Total Orders: ", result
