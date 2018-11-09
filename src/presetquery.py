import pyxl
import mysql.connector

from pypika import MySQLQuery, Table, Field

def get_preset(conn, key):
	# the use of this function assumes there exists some Table
	# called Presets where the first column is an
	# UNSIGNED AUTO_INCREMENT PRIMARY KEY labeled id
	# and the second column is a VARCHAR NOT NULL labeled querval
	# to use this method you must pass in a connection
	# and the id for the corresponding querval to return
	# The querval returned is formatted to be ready to use
	# as a query
	cursor = conn.cursor()
	quer = "ALTER TABLE Presets DROP COLUMN id;"
	cursor.execute(quer)
	quer = "ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY;"
	cursor.execute(quer)
	
	extable = Table('Presets')
	q = MySQLQuery.from_(extable).select(
		extable.querval
	).where(
		extable.id == key
	)
	print(q)
	quer = str(q)

	cursor.execute(quer)
	
	row = cursor.fetchone()
	strrow = str(row)
	
	
	
	
	return (strrow[2:-3])
