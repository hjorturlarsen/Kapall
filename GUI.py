#!/usr/bin/env python
# encoding: utf-8

import os, pygame, math, sys, random
import time as tm 
from pygame import *
import menu, GUI, Deck, Card, Golf_relaxed
from Golf_relaxed import *

class GUI:
	def __init__(self):

		the_timeSec = 0.0
		the_timeMin = 0.0
		the_score = 0

		pygame.init()
		self.screen = pygame.display.set_mode((800, 500))
		pygame.display.set_caption('Gooby plz')
		pygame.mouse.set_visible(1)
		background = pygame.image.load("data/dolanbackground.png")
		backgroundRect = background.get_rect()


		self.game = Golf_relaxed()
		
		self.collumns = [self.game.col1.sprites(), self.game.col2.sprites(), self.game.col3.sprites(), self.game.col4.sprites(), self.game.col5.sprites(), self.game.col6.sprites(), self.game.col7.sprites()]
		allsprites =  pygame.sprite.LayeredDirty((self.game.deckA, self.game.deckB, self.game.col1, self.game.col2, self.game.col3, self.game.col4, self.game.col5, self.game.col6, self.game.col7))
		allsprites.clear(self.screen, background)


		clock = pygame.time.Clock()

		# MENU
		ourMenu = ["Start"]

		myMenu = menu.Menu(ourMenu, 'data/dolanbackground.png')
		myMenu.drawMenu()

		# Display score
		font = pygame.font.Font(None, 36)
		text = font.render("Score: %d" % (the_score), 1, (255, 255, 255))
		textpos = text.get_rect()
		textpos.center = (700, 475)
		self.screen.blit(text, textpos)

		# Display time
		start = tm.time()
		textTime = font.render("Time: %.0f : %.0f" % (the_timeMin, the_timeSec), 1, (255, 255, 255))
		textposTime = textTime.get_rect()
		textposTime.center = (100, 475)
		self.screen.blit(textTime, textposTime)


		self.MouseLPressed = False
		# MAINLOOP
		while 1:
			#Timateljari
			end = tm.time()
			tm.sleep(0.1)
			the_timeSec = end-start
			if the_timeSec > 60:
				the_timeMin = the_timeSec / 60
				the_timeSec = 0
			textTime = font.render("Time: %.0f : %.0f" % (the_timeMin, the_timeSec), 1, (255, 255, 255))

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

			self.screen.blit(background, (0, 0))
			if myMenu.isActive():
				myMenu.drawMenu()

			#TEIKNA HLUTI
			else:
				self.screen.blit(background, backgroundRect)
				rects = allsprites.draw(self.screen)
				pygame.display.update(rects)

				self.update()

				if event.type == MOUSEBUTTONDOWN:
					self.MouseLPressed = True
					for idx, card in enumerate(self.game.deckA):
						if card.clicked(event.pos):
							if len(self.game.deckA.sprites()) > 0:
								self.game.deckB.add(card)
								self.game.deckA.remove(card)
							#50 stig ef ytt er a bunka A
							the_score += 50
							text = font.render("Score: %d" % (the_score), 1, (255, 255, 255))							


				if event.type == MOUSEBUTTONUP:
					self.MouseLPressed = False
					self.set_up_deckB()
					self.set_up_deckA()

				#Update score and time
				self.screen.blit(text, textpos)
				self.screen.blit(textTime, textposTime)

				if self.MouseLPressed == True:
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							card.clicked(event.pos)




			pygame.display.flip()

	def update(self):
		deckA = self.game.deckA.sprites()
		deckB = self.game.deckB.sprites()
		for idx, col in enumerate(self.collumns):
			for idx2, card in enumerate(col):
				card.dirty = 1
		for idx, card in enumerate(deckA):
			card.dirty = 1
		for idx, card in enumerate(deckB):
			card.dirty = 1

	def set_up_collumns(self):
		col1 = self.game.col1.sprites()
		col2 = self.game.col2.sprites()
		col3 = self.game.col3.sprites()
		col4 = self.game.col4.sprites()
		col5 = self.game.col5.sprites()
		col6 = self.game.col6.sprites()
		col7 = self.game.col7.sprites()
		collumns = [col1, col2, col3, col4, col5, col6, col7]
		x = 50
		for idx, col in enumerate(collumns):
			y = 15
			for idx2, card in enumerate(col):
				card.rect.x = x
				card.rect.y = y
				card.image = card.frontImg
				y += 30
			x += 100
			if len(col) > 0:
				col[-1].selectable = True

	def set_up_deckA(self):
		deckA = self.game.deckA.sprites()
		x = 50
		y = 300
		for card in deckA:
			card.rect.x = x
			card.rect.y = y
			card.image = card.backImg
			card.dirty = 1
		if len(deckA) > 0:
			deckA[-1].selectable = True
	
	def set_up_deckB(self):
		x = 150
		y = 300
		cards = ""

		for card in self.game.deckB.sprites():
			cards += card.id + " "
			card.rect.x = x
			card.rect.y = y
			card.image = card.frontImg
			card.selectable = False
			x += 10
		print cards

