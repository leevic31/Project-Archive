import pyxl
import mysql.connector

from pypika import MySQLQuery, Table, Field

def write_preset(conn, queryin, descriptin):
	# the use of this function assumes there exists some Table
	# called 'Presets' where the first column is an
	# UNSIGNED AUTO_INCREMENT PRIMARY KEY labeled 'id'
	# and the second column is a VARCHAR NOT NULL labeled 'querval'
	# and the third column is a VARCHAR NOT NULL labeled 'description'
	
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
	
