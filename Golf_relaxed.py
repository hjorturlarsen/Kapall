#!/usr/bin/env python
# encoding: utf-8

import Card, Deck, Group_of_cards
from Group_of_cards import *
from Deck import *
import pygame
from pygame import *

class Golf_relaxed:
	def __init__(self):
		self.deck = Deck()
		self.deckA = Group_of_cards()
		self.deckB = Group_of_cards()
		self.col1 = Group_of_cards()
		self.col2 = Group_of_cards()
		self.col3 = Group_of_cards()
		self.col4 = Group_of_cards()
		self.col5 = Group_of_cards()
		self.col6 = Group_of_cards()
		self.col7 = Group_of_cards()
		self.set_up_game()
		
	def set_up_game(self):
		for card in range(0,5):
			self.col1.add(self.deck.get())
			self.col2.add(self.deck.get())
			self.col3.add(self.deck.get())
			self.col4.add(self.deck.get())
			self.col5.add(self.deck.get())
			self.col6.add(self.deck.get())
			self.col7.add(self.deck.get())
		self.deckB.add(self.deck.get())
		self.deckA.group = self.deck.deck