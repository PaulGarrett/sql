

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    c.execute("""CREATE TABLE orders
     (make TEXT, model TEXT, order_date DATE)""")
    
    orders = [
            ('Ford','Mustang','2014-02-01'),
            ('Ford','Mustang','2014-04-11'),
            ('Ford','Alpine','2014-01-21'),
            ('Ford','Mustang','2014-06-11'),
            ('Ford','Alpine','2014-04-15'),
            ('Ford','Alpine','2014-06-05'),
            ('Ford','Fairlaine','2014-02-25'),
            ('Ford','Fairlaine','2014-03-15'),
            ('Ford','Fairlaine','2014-04-03'),
            ('Honda','Civic','2014-02-05'),
            ('Honda','Civic','2014-04-20'),
            ('Honda','Civic','2014-06-15'),
            ('Honda','Accord','2014-02-15'),
            ('Honda','Accord','2014-02-25'),
            ('Honda','Accord','2014-05-07'),
            ]
    c.executemany("INSERT INTO orders VALUES(?, ?,? )", orders)        

    c.execute("SELECT * FROM orders ORDER BY order_date ASC")

    rows = c.fetchall()

    for r in rows:
    	print r[0], r[1], r[2]
