#!/usr/bin/env python
# encoding: utf-8

import os, pygame, math, sys, random, time
from pygame.locals import *
import menu, GUI, Deck, Card, Group_of_cards, Golf_relaxed
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
		

		allsprites = pygame.sprite.RenderPlain(self.game.col1)

		clock = pygame.time.Clock()

		# MENU
		ourMenu = ["Start", "Quit"]

		myMenu = menu.Menu(ourMenu)
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

						self.set_up_collumns()
						self.set_up_deckA()
						self.set_up_deckB()

					#QUIT
					if event.item == 1:
						return

			self.screen.blit(background, (0, 0))
			if myMenu.isActive():
				myMenu.drawMenu()
			#TEIKNA HLUTI
			else:
				self.screen.blit(background, backgroundRect)

				self.draw_all(self.screen)

				if event.type == MOUSEBUTTONDOWN:
					self.MouseLPressed = True


				if event.type == MOUSEBUTTONUP:
					self.MouseLPressed = False


				#if self.MouseLPressed == True:
					#for card
					#self.game.col1.clicked(event.pos)
					#for object in self.game.col1.group:
					#	object.clicked(event.pos)

			pygame.display.flip()

	def draw_all(self, surface):
		self.game.col1.draw(surface)
		self.game.col2.draw(surface)
		self.game.col3.draw(surface)
		self.game.col4.draw(surface)
		self.game.col5.draw(surface)
		self.game.col6.draw(surface)
		self.game.col7.draw(surface)
		self.game.deckA.draw(surface)
		self.game.deckB.draw(surface)


	def set_up_collumns(self):
		col1 = self.game.col1.group 
		col2 = self.game.col2.group
		col3 = self.game.col3.group
		col4 = self.game.col4.group
		col5 = self.game.col5.group
		col6 = self.game.col6.group
		col7 = self.game.col7.group
		collumns = [col1, col2, col3, col4, col5, col6, col7]
		x = 50
		for col_idx, collumn in enumerate(collumns):
			y = 15
			for card in collumn:
				card.rect.x = x
				card.rect.y = y
				card.img = card.frontImg
				y += 30
			x += 100
			collumn[-1].selectable = True

	def set_up_deckA(self):
		x = 50
		y = 300
		for card in self.game.deckA.group:
			card.rect.x = x
			card.rect.y = y
			card.img = card.backImg
		self.game.deckA.group[-1].selectable = True
	
	def set_up_deckB(self):
		x = 150
		y = 300
		for card in self.game.deckB.group:
			card.rect.x = x
			card.rect.y = y
			card.img = card.frontImg
			x += 10
