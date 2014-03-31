#!/usr/bin/env python
# encoding: utf-8

import Card, Deck
from Deck import *
import pygame
from pygame import *

class Golf_relaxed:
	def __init__(self):
		self.deck = Deck()
		self.deckA = pygame.sprite.Group()
		self.deckB = pygame.sprite.Group()
		self.collumns = pygame.sprite.Group()
		self.set_up_game()
		
	def set_up_game(self):
		for i in range(0,35):
			self.collumns.add(self.deck.get())
		self.deckB.add(self.deck.get())
		for i in range(0,16):
			self.deckA.add(self.deck.get())