# -*- coding: cp1252 -*-
import sqlite3

# Variables for DB
ident = raw_input("id: ")
initials = unicode(raw_input("Initials: "), 'utf-8') # Can use Unicode characters
score = raw_input("Score: ")
time = raw_input("Time: ")

# Only inserts into DB if initials are 3 characters
if(len(initials) == 3):
	# Make a connection
	conn = sqlite3.connect('highscore.db')
	c = conn.cursor()

	# Insert into DB 
	info = (ident, initials, score, time)
	c.execute("INSERT INTO highscore VALUES (?, ?, ?, ?)", info)

	# Commit before closing
	conn.commit()
	# Always close after we finish
	conn.close()

else:
	print "Error your initials must be 3 characters"