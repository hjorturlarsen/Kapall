#!/usr/bin/env python
# encoding: utf-8

class Deck_B:
	def __init__(self):
		self.deck_b = []

	def __str__(self):
		return self.deck_b

	def add_card(self, card):
		self.deck_b.append(card)

	def draw(self, surface):
		for card in self.deck_b:
			surface.blit(card.img, card.rect.topleft)

	def clickCheck(self, pos):
		for object in self.deck_b:
			if object.rect.collidepoint(pos):
				if object.selectable:
					return True