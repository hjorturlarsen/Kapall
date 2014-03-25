# -*- coding: cp1252 -*-
import sqlite3

def databaseCall():
	conn = sqlite3.connect('highscore.db')
	conn.text_factory = str
	c = conn.cursor()

	c.execute("SELECT initials, score, time FROM highscore ORDER BY score DESC, time ASC")

	row = c.fetchall()

	# Birtir top 15
	count = 1
	strengur = ""
	totalString = ""
	for member in row:
		if len(str(member[1])) == 5:
			length = "    "
		if len(str(member[1])) == 4:
			length = "     "
		if len(str(member[1])) == 3:
			length = "      "
		if len(str(member[1])) == 2:
			length = "       "
		if len(str(count)) == 1:
			length2 = ".  "
		if len(str(count)) == 2:
			length2 = ". "
		strengur = str(count) + length2 + str(member[0]) + "    " + str(member[1]) + length + str(member[2]) + "\n"
		totalString += strengur
		count += 1
		if count == 16:
			break
	f = open('highscore.txt', 'w')
	f.write(totalString)

	# Commit before closing
	conn.commit()
	# Always close after we finish
	conn.close()

databaseCall()
