#INSERT Command (compact form)

# import the sqlite3 library
import sqlite3

#create connection object 

with sqlite3.connect("new.db") as connection:
# get cursor object to execute sql commands

	c=connection.cursor()

#insert data
	c.execute("INSERT INTO population VALUES('New York City','NY',8200000)")
	c.execute("INSERT INTO population VALUES('San Francisco','CA',8000000)")
