# SQLite Functions

"""Using the COUNT() function, calculate the total number of orders for each make and model."""

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # create a dictionary of sql queries
    sql = {'Ford Mustang count'    : "SELECT count(make) FROM orders WHERE model = 'Mustang'",
           'Ford Alpine count'    : "SELECT count(make) FROM orders WHERE model = 'Alpine'",
           'Ford Fairlaine count'    : "SELECT count(make) FROM orders WHERE model = 'Fairlaine'",
           'Honda Civic count'   : "SELECT count(make) FROM orders WHERE model = 'Civic'",
           'Honda Accord count'  : "SELECT count(make) FROM orders WHERE model = 'Accord'",}
        
    # run each sql query item in the dictionary
    for keys, values in sql.iteritems():

        # run sql
        c.execute(values)

        # fetchone() retrieves one record from the query
        result = c.fetchone()

        # output the result to screen
        print keys + ":", result[0]