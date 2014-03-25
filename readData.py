# -*- coding: cp1252 -*-
import sqlite3

def databaseCall():
	conn = sqlite3.connect('highscore.db')
	conn.text_factory = str
	c = conn.cursor()

	c.execute("SELECT initials, score, time FROM highscore ORDER BY score DESC, time ASC")

	row = c.fetchall()

	# Birtir top 15
	count = 0
	for member in row:
		print member[0], member[1], member[2]
		count += 1
		if count == 15:
			break

	# Commit before closing
	conn.commit()
	# Always close after we finish
	conn.close()
databaseCall()