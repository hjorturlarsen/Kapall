#!/usr/bin/env python
# encoding: utf-8

import Card
import random
import pygame
from pygame import *

class Group_of_cards(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.group = []

	def __str__(self):
		return self.group

	def isEmpty(self):
		if(len(self.group) == 0):
			return True
		else:
			return False

	def get(self):
		if not self.isEmpty():
			return self.group.pop()

	def draw(self, surface):
		for card in self.group:
			card.draw(surface)

	def add(self, card):
		self.group.append(card)
		
	def clicked(self, pos):
		for card in self.group:
			if card.rect.collidepoint(pos):
				return True