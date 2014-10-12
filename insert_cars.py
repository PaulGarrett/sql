# import from CSV

# import the csv library
import csv

import sqlite3

with sqlite3.connect("cars.db") as connection:
	c=connection.cursor()

	# open the csv file and assign it to a variable

	newcars = csv.reader(open("newcars.csv", "rU"))
		# insert data into table
	c.executemany("INSERT INTO inventory(Make, Model, Quantity) values (?,?,?)", newcars)