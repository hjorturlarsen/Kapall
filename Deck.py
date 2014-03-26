#!/usr/bin/env python
# encoding: utf-8

import Card
import random
import pygame
from pygame import *

class Deck(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.deck = []
		self.create_deck()
		self.apply_images()
		self.shuffle_deck()


	def __str__(self):
		return self.deck.deck

	#N: self.Deck = self.createDeck()
	#F: Ekkert
	#E: Buid er ad bua til spilastokk med 52 spilum
	def create_deck(self):
		suit = ['H', 'L', 'S', 'T']
		rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

		for s in suit:
			for r in rank:
				self.deck.append(s+`r`)
		return self.deck

	def apply_images(self):
		for idx, card in enumerate(self.deck):
			self.deck[idx] = Card.Card(self.deck[idx])
		return self.deck


	def shuffle_deck(self):
		random.shuffle(self.deck)
		return self.deck

	#N: self.deck.isEmpty()
	#F: self.deck er spilabúnki
	#E: True ef búnkinn er ekki tómur, annars False
	def isEmpty(self):
		if(len(self.deck) == 0):
			return True
		else:
			return False

	#N: self.deck.get_card()
	#F: self.deck er búnki með spilum
	#E: Búið er að draga aftasta spilið úr búnkanum
	def get_card(self):
		if not self.isEmpty():
			return self.deck.pop()

	def draw(self, surface):
		for card in self.deck:
			card.draw(surface)

	def clickCheck(self, pos):
		for card in self.deck:
			if card.rect.collidepoint(pos):
				print "COLLISION " + card.id
