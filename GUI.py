#!/usr/bin/env python
# encoding: utf-8

import os, pygame, math, sys, random, time
from pygame import *
import menu, GUI, Deck, Card, Golf_relaxed
from Golf_relaxed import *

class GUI:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 500))
		pygame.display.set_caption('Gooby plz')
		pygame.mouse.set_visible(1)
		background = pygame.image.load("data/dolanbackground.png")
		backgroundRect = background.get_rect()


		self.game = Golf_relaxed()
		
		allsprites =  pygame.sprite.LayeredDirty((self.game.deckA, self.game.deckB, self.game.collumns))
		allsprites.clear(self.screen, background)


		clock = pygame.time.Clock()

		# MENU
		ourMenu = ["Start"]

		myMenu = menu.Menu(ourMenu, 'data/dolanbackground.png')
		myMenu.drawMenu()


		self.MouseLPressed = False
		# MAINLOOP
		while 1:
		# INPUT EVENTS
			for event in pygame.event.get():
				myMenu.handleEvent(event)
				# QUIT TO MENU
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					myMenu.activate()
				elif event.type == menu.Menu.MENUCLICKEDEVENT:
					#START AND INITIALIZE GAME
					if event.item == 0:
						isGameActive = True
						myMenu.deactivate()

			self.screen.blit(background, (0, 0))
			if myMenu.isActive():
				myMenu.drawMenu()
			#TEIKNA HLUTI
			else:
				self.screen.blit(background, backgroundRect)
				rects = allsprites.draw(self.screen)
				pygame.display.update(rects)
				self.set_up_collumns()
				self.set_up_deckA()
				self.set_up_deckB()

				if event.type == MOUSEBUTTONDOWN:
					self.MouseLPressed = True


				if event.type == MOUSEBUTTONUP:
					self.MouseLPressed = False


				if self.MouseLPressed == True:
					for card in self.game.collumns.sprites(), self.game.deckA.sprites():
						print card

			pygame.display.flip()

	def set_up_collumns(self):
		x = 50
		y = 15
		collumns = self.game.collumns.sprites()
		for idx, card in enumerate(collumns):
			index = idx+1
			card.rect.x = x
			card.rect.y = y
			card.image = card.frontImg
			y += 30
			if idx > 0 and index % 5 == 0:
				x += 100
				y = 15
			card.dirty = 1

	def set_up_deckA(self):
		x = 50
		y = 300
		for card in self.game.deckA.sprites():
			card.rect.x = x
			card.rect.y = y
			card.image = card.backImg
			card.dirty = 1
	
	def set_up_deckB(self):
		x = 150
		y = 300
		for card in self.game.deckB.sprites():
			card.rect.x = x
			card.rect.y = y
			card.image = card.frontImg
			x += 10
			card.dirty = 1
