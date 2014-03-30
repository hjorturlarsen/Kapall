#!/usr/bin/env python
# encoding: utf-8
import pygame
from pygame import *
import os

class Card(pygame.sprite.Sprite):
	def __init__(self, id):
		pygame.sprite.Sprite.__init__(self)
		self.id = str(id)
		self.backImg = self.load_image('b')
		self.frontImg = self.load_image(id)
		self.img = self.backImg
		self.rect = self.backImg.get_rect()
		self.rect.x = 0
		self.rect.y = 0
		self.selected = False
		self.selectable = False
		
		if (int(id[1:] == 13)):
			self.parent = id[:1] + "1"
		else:
			rank_int = int(id[1:])+1
			rank_str = str(rank_int)
			self.parent = id[:1] + rank_str

		if (int(id[1:] == 1)):
			self.child = id[:1] + "13"
		else:
			rank_int = int(id[1:])-1
			rank_str = str(rank_int)
			self.child = id[:1] + rank_str

	def __str__(self):
		return self.id

	def load_image(self, name, colorkey=None):
		name = name+'.png'
		fullname = os.path.join('data', name)
		try:
			image = pygame.image.load(fullname)
		except pygame.error, message:
			print 'Cannot load image:', name
			raise SystemExit, message
		image = image.convert()
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, RLEACCEL)
		return image

	def draw(self,surface):
		surface.blit(self.img,self.rect.topleft)