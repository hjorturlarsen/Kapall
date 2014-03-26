#!/usr/bin/env python
# encoding: utf-8

import os, pygame, math, sys, random, time
from pygame.locals import *
import menu, GUI, Board, Deck_B, Deck, Card

class GUI:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 500))
		pygame.display.set_caption('Gooby plz')
		pygame.mouse.set_visible(1)
		background = pygame.image.load("data/dolanbackground.png")
		backgroundRect = background.get_rect()

		self.deck_a = Deck.Deck()
		self.deck_b = Deck_B.Deck_B()
		self.board = Board.Board()
		self.deck_a_selectable()

		allsprites = pygame.sprite.RenderPlain((self.deck_a))
		clock = pygame.time.Clock()

		# MENU
		ourMenu = ["Start", "Quit"]

		myMenu = menu.Menu(ourMenu)
		myMenu.drawMenu()


		MouseLPressed = False
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

						#SÝNA SPIL
						self.set_up_board(self.screen)
						self.set_up_deck_a(self.screen)
						self.set_up_deck_b(self.screen)
					#QUIT
					if event.item == 1:
						return

			self.screen.blit(background, (0, 0))
			if myMenu.isActive():
				myMenu.drawMenu()
			#TEIKNA HLUTI
			else:
				allsprites.update()
				#allsprites.draw(self.screen)
				self.screen.blit(background, backgroundRect)
				self.deck_a.draw(self.screen)
				self.deck_b.draw(self.screen)
				self.board.draw(self.screen)
				if event.type == MOUSEBUTTONDOWN:
					MouseLPressed = True

				if event.type == MOUSEBUTTONUP:
					MouseLPressed = False
					if self.deck_a.clickCheck(event.pos):
						deck_a_pop = self.deck_a.get_card()
						self.deck_b.add_card(deck_a_pop)
						self.set_up_deck_b(self.screen)
						self.set_up_deck_a(self.screen)
					self.deck_a_selectable()

				if MouseLPressed == True:
					for object in self.deck_a, self.board:
						object.clickCheck(event.pos)


		    	pygame.display.flip()

	def set_up_board(self, surface):
			x = 50
			if(not self.deck_a.isEmpty()):
				for col_idx, collumn in enumerate(self.board.board):
					y = 15
					for i in range(0,5):
						card = self.deck_a.get_card()
						card.rect.x = x
						card.rect.y = y
						card.img = card.frontImg
						collumn[i] = card

						if i == 4:
							card.selectable = True
							
						y+=30
					x += 100
				self.deck_b.add_card(self.deck_a.get_card())

	def set_up_deck_a(self, surface):
		x = 50
		y = 300
		for card in self.deck_a.deck:
			card.rect.x = x
			card.rect.y = y
			card.img = card.backImg
	
	def deck_a_selectable(self):
		if len(self.deck_a.deck) > 0:
			self.deck_a.deck[-1].selectable = True


	def set_up_deck_b(self, surface):
		x = 150
		y = 300
		for card in self.deck_b.deck_b:
			card.rect.x = x
			card.rect.y = y
			card.img = card.frontImg
			x += 20
			card.selectable = False