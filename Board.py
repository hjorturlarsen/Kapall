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

	def isEmpty(self, id):
		if(len(self.board[id]) == 0):
			return True
		else:
			return False

	def clickCheck(self, pos):
		for collumn in self.board:
			for card in collumn:
				if card.selected:
					card.rect.center = pos

	def select_card(self, pos):
		for collumn in self.board:
			for card in collumn:
				if card.selectable:
					if card.rect.collidepoint(pos):
						card.selected = True