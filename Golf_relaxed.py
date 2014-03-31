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
		self.col1 = pygame.sprite.Group()
		self.col2 = pygame.sprite.Group()
		self.col3 = pygame.sprite.Group()
		self.col4 = pygame.sprite.Group()
		self.col5 = pygame.sprite.Group()
		self.col6 = pygame.sprite.Group()
		self.col7 = pygame.sprite.Group()
		self.set_up_game()
		
	def set_up_game(self):
		for i in range(0,5):
			self.col1.add(self.deck.get())
			self.col2.add(self.deck.get())
			self.col3.add(self.deck.get())
			self.col4.add(self.deck.get())
			self.col5.add(self.deck.get())
			self.col6.add(self.deck.get())
			self.col7.add(self.deck.get())
		self.deckB.add(self.deck.get())
		for i in range(0,16):
			self.deckA.add(self.deck.get())