#!/usr/bin/env python
# encoding: utf-8

import Card
import random
import pygame
from pygame import *

class Deck(pygame.sprite.DirtySprite):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.deck = []
		self.create_deck()
		self.apply_images()
		self.shuffle_deck()

	def __str__(self):
		return self.deck

	def create_deck(self):
		suit = ['H', 'L', 'S', 'T']
		rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

		for s in suit:
			for r in rank:
				self.deck.append(s+`r`)
		self.deck.append('W21')
		return self.deck

	def shuffle_deck(self):
		random.shuffle(self.deck)
		return self.deck

	def get(self):
		if not self.isEmpty():
			return self.deck.pop()

	def isEmpty(self):
		if(len(self.deck) == 0):
			return True
		else:
			return False

	def apply_images(self):
		for idx, card in enumerate(self.deck):
			self.deck[idx] = Card.Card(self.deck[idx])
		return self.deck