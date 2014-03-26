#!/usr/bin/env python
# encoding: utf-8

class Board:
	def __init__(self):
		self.board = [[0,0,0,0,0] for collumn in range (7)]

	def __str__(self):
		result = "\n".join("\t".join(map(str,l)) for l in self.board)
		return result

	def draw(self, surface):
		for collumn in self.board:
			for card in collumn:
				card.draw(surface)

	#N: self.board[x].isEmpty()
	#F: self.board er listi af listum, þar sem ytri listinn er að lengd 7
	#		og innri listarnir eru af lengd 5.
	#E: True ef innri listi x er tómnur, annars False
	def isEmpty(self, id):
		if(len(self.board[id]) == 0):
			return True
		else:
			return False

	def clickCheck(self, pos):
		for collumn in self.board:
			for card in collumn:
				if card.rect.collidepoint(pos):
					if card.selectable:
						print "COLLISION " + card.id
					else:
						return