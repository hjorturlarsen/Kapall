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
		allsprites =  pygame.sprite.LayeredUpdates((self.game.deckB, self.game.deckA, self.game.col1, self.game.col2, self.game.col3, self.game.col4, self.game.col5, self.game.col6, self.game.col7))
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
			#Timi
			end = tm.time()
			tm.sleep(0.01)
			the_timeSec = end-start
			the_timeMin = int(the_timeSec/60)
			the_timeSec2 = int(the_timeSec % 60)
			textTime = font.render("Time: %.0f : %.0f" % (the_timeMin, the_timeSec2), 1, (255, 255, 255))

		# INPUT EVENTS
			for event in pygame.event.get():
				myMenu.handleEvent(event)

				# QUIT TO MENU
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					#SKRÁ NAFN!!!!!!
					#print self.ask(self.screen, "Name")
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
				allsprites.draw(self.screen)
				#pygame.display.update(rects)
				self.update()

				if event.type == MOUSEBUTTONDOWN:
					self.MouseLPressed = True
					for idx, card in enumerate(self.game.deckA.sprites()):
						if card.clicked(event.pos):
							if len(self.game.deckA.sprites()) > 0:
								self.game.deckB.add(card)
								self.game.deckA.remove(card)
							#50 points if clicked on deck A
							the_score += 50
							text = font.render("Score: %d" % (the_score), 1, (255, 255, 255))
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							if card.selectable:
								card.clicked(event.pos)
								

				if event.type == MOUSEBUTTONUP:
					self.MouseLPressed = False
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							if card.selected:
								card.selected = False

					self.set_up_deckB()
					self.set_up_deckA()

				#Update time and score
				self.screen.blit(text, textpos)
				self.screen.blit(textTime, textposTime)

				if self.MouseLPressed == True:
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							card.move(event.pos)




			pygame.display.flip()

	def update(self):
		deckA = self.game.deckA.sprites()
		deckB = self.game.deckB
		#for idx, col in enumerate(self.collumns):
		#	for idx2, card in enumerate(col):
		#		card.dirty = 1
		for idx, card in enumerate(deckA):
			card.draw(self.screen)
		for idx, card in enumerate(deckB):
			card.draw(self.screen)

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
		deckB = self.game.deckB
		for card in deckB:
			card.rect.x = x
			card.rect.y = y
			card.image = card.frontImg
			card.selectable = False
			x += 10

	def get_key(self):
		while 1:
			event = pygame.event.poll()
			if event.type == KEYDOWN:
				return event.key
			else:
				pass

	def display_box(self, screen, message):
		fontobject = pygame.font.Font(None,18)
		pygame.draw.rect(screen, (0,0,0), ((screen.get_width() / 2) - 100 ,(screen.get_height() / 2) + 140,200,20), 0)
		pygame.draw.rect(screen, (255,255,255),((screen.get_width() / 2) - 102,(screen.get_height() / 2) + 138,204,24), 1)
		if len(message) != 0:
			screen.blit(fontobject.render(message, 1, (255,255,255)),((screen.get_width() / 2) - 100, (screen.get_height() / 2) +144))
		pygame.display.flip()


	def ask(self, screen, question):
		pygame.font.init()
		current_string = ""
		self.display_box(screen, question + ": " + current_string)
		while 1:
			inkey = self.get_key()
			if inkey == K_BACKSPACE:
				current_string = current_string[:len(current_string)-1]
			elif inkey == K_RETURN:
				break
			#elif inkey == K_MINUS:
				current_string.append("_")
			elif inkey <= 127:
				current_string = current_string + chr(inkey)
			self.display_box(screen, question + ": " + current_string)
		return current_string
