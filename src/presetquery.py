import pyxl
import mysql.connector

from pypika import MySQLQuery, Table, Field

	# the use of this function assumes there exists some Table
	# called 'Presets' where the first column is an
	# UNSIGNED AUTO_INCREMENT PRIMARY KEY labeled 'id'
	# and the second column is a VARCHAR NOT NULL labeled 'querval'
	# and the third column is a VARCHAR NOT NULL labeled 'description'
	
def write_preset(conn, queryin, descriptin):	
	# to use this method you must pass in a connection,
	# a preset query, and a description of what the query achieves
	# it will automatically write it to the bottom of the table
	cursor = conn.cursor()
	quer = "ALTER TABLE Presets DROP COLUMN id;"
	cursor.execute(quer)
	quer = "ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;"
	cursor.execute(quer)
	
	extable = Table('Presets')
	q = MySQLQuery.into(extable).columns("querval", "description").insert(queryin, descriptin)
	print(q)
	quer = str(q)
	
	cursor.execute(quer)
	
	cursor = conn.cursor()
	quer = "ALTER TABLE Presets DROP COLUMN id;"
	cursor.execute(quer)
	quer = "ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;"
	cursor.execute(quer)
	
def get_preset(conn, key):
	# to use this method you must pass in a connection
	# and the id for the corresponding querval to return
	# The querval returned is formatted to be ready to use
	# as a query
	cursor = conn.cursor()
	quer = "ALTER TABLE Presets DROP COLUMN id;"
	cursor.execute(quer)
	quer = "ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;"
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
	
def get_descriptin(conn, key):
	# to use this method you must pass in a connection
	# and the id for the corresponding description to return
	# The description returned is formatted to be ready to displayed
	cursor = conn.cursor()
	quer = "ALTER TABLE Presets DROP COLUMN id;"
	cursor.execute(quer)
	quer = "ALTER TABLE Presets ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY NOT NULL FIRST;"
	cursor.execute(quer)
	
	extable = Table('Presets')
	q = MySQLQuery.from_(extable).select(
		extable.description
	).where(
		extable.id == key
	)
	print(q)
	quer = str(q)

	cursor.execute(quer)
	
	row = cursor.fetchone()
	strrow = str(row)
	
	return (strrow[2:-3])
	
