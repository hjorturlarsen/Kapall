#!/usr/bin/env python
# encoding: utf-8



#---------- SKIPUN TIL AÐ VISTA Í GAGNAGRUNN
#HighScoreInsertion.insertHighscore(ident, initials, score, time)

import os, pygame, math, sys, random
import time as tm
from pygame import *
import menu, GUI, Deck, Card, Golf_relaxed
from Golf_relaxed import *
import HighScoreInsertion

class GUI:
	def __init__(self):

		global the_timeSec
		the_timeSec = 0.0
		global the_timeMin
		the_timeMin = 0.0
		global the_score 
		the_score = 0
		score_multiplier = 0

		pygame.init()
		self.screen = pygame.display.set_mode((800, 500))
		pygame.display.set_caption('Gooby plz')
		pygame.mouse.set_visible(1)
		background = pygame.image.load("data/dolanbackground.png")
		backgroundRect = background.get_rect()

		self.game = Golf_relaxed()
		
		self.collumns = [self.game.col1.sprites(), self.game.col2.sprites(), self.game.col3.sprites(), self.game.col4.sprites(), self.game.col5.sprites(), self.game.col6.sprites(), self.game.col7.sprites()]
		allsprites =  pygame.sprite.LayeredUpdates((self.game.col1, self.game.col2, self.game.col3, self.game.col4, self.game.col5, self.game.col6, self.game.col7))
		allsprites.clear(self.screen, background)

		#Old position of card
		self.old_pos = None

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
					myMenu.activate()
				elif event.type == menu.Menu.MENUCLICKEDEVENT:

					#START AND INITIALIZE GAME
					if event.item == 0:
						isGameActive = True
						myMenu.deactivate()

						self.set_up_collumns()
						self.set_up_deckA()
						self.set_up_deckB()
						self.selectable_collumns()

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

							# 50 points if clicked on deck A
							# and multiplier given the value 0
							the_score += 50
							score_multiplier = 0
							text = font.render("Score: %d" % (the_score), 1, (255, 255, 255))
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							if card.selectable:
								card.clicked(event.pos)

				if event.type == MOUSEBUTTONUP:
					self.MouseLPressed = False
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							###LOOOSEERRR#####################################
							#THARF AD LAGA FYRIR EFSTU LINU OG WILDCARD
							last_B = self.game.deckB.sprites()[-1]
							if len(self.game.deckA) == 0:
								if (int(self.collumns[0][-1].rank) != last_B.child and int(self.collumns[0][-1].rank) != last_B.parent and int(self.collumns[0][-1].rank) != 21):
									if (int(self.collumns[1][-1].rank) != last_B.child and int(self.collumns[1][-1].rank) != last_B.parent and int(self.collumns[0][-1].rank) != 21):
										if (int(self.collumns[2][-1].rank) != last_B.child and int(self.collumns[2][-1].rank) != last_B.parent and int(self.collumns[0][-1].rank) != 21):
											if (int(self.collumns[3][-1].rank) != last_B.child and int(self.collumns[3][-1].rank) != last_B.parent and int(self.collumns[0][-1].rank) != 21):
												if (int(self.collumns[4][-1].rank) != last_B.child and int(self.collumns[4][-1].rank) != last_B.parent and int(self.collumns[0][-1].rank) != 21):
													if (int(self.collumns[5][-1].rank) != last_B.child and int(self.collumns[5][-1].rank) != last_B.parent and int(self.collumns[0][-1].rank) != 21):
														if (int(self.collumns[6][-1].rank) != last_B.child and int(self.collumns[6][-1].rank) != last_B.parent and int(self.collumns[0][-1].rank) != 21):

																print "OMG EG TAPADI"
																#print self.collumns[idx2][4]#.col[4]

							##################################################
							if card.selected:
								card.selected = False

								#Collision Detection
								last_in_deckB = self.game.deckB.sprites()[-1]
								if pygame.sprite.collide_rect(card, last_in_deckB) and (last_in_deckB.child == int(card.rank) or last_in_deckB.parent == int(card.rank)):
									self.game.deckB.add(card)
									col.pop()
									self.selectable_collumns()
									
									# Each tima a player can remove more
									# than 1 card from the board in a row the
									# score will be multiplied be a higher number
									score_multiplier += 1
									the_score += 100 + math.pow(score_multiplier, 4)
									text = font.render("Score: %d" % (the_score), 1, (255, 255, 255))
									# elif loops are for the wildcard
								elif pygame.sprite.collide_rect(card, last_in_deckB) and last_in_deckB.id == 'W21':
									col.pop()
									self.selectable_collumns()
									self.game.deckB.add(card)
									the_score += 5000
									text = font.render("Score: %d" % (the_score), 1, (255, 255, 255))
								elif pygame.sprite.collide_rect(card, last_in_deckB) and card.id == 'W21':
									col.pop()
									self.selectable_collumns()
									self.game.deckB.add(card)
								else:
									card.rect.x = self.old_pos[0]
									card.rect.y = self.old_pos[1]

					self.set_up_deckB()
					self.set_up_deckA()

				#Update time and score
				self.screen.blit(text, textpos)
				self.screen.blit(textTime, textposTime)

				if self.MouseLPressed == True:
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							card.move(event.pos)

				if self.MouseLPressed == False:
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							if card.selectable:
								if card.rect.collidepoint(mouse.get_pos()):
									self.old_pos = (card.rect.x, card.rect.y)


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
		x = 50
		for idx, col in enumerate(self.collumns):
			y = 15
			for idx2, card in enumerate(col):
				card.rect.x = x
				card.rect.y = y
				card.image = card.frontImg
				y += 30
			x += 100

	def selectable_collumns(self):
		for idx, col in enumerate(self.collumns):
			if len(col) > 0:
				col[-1].selectable = True
		##WINNNNNERR
		#Tharf ad lagfaera fyrir skor
		dresl = 0
		dresl = len(self.collumns[0]+self.collumns[1]+self.collumns[2]+self.collumns[3]+self.collumns[4]+self.collumns[5]+self.collumns[6])
		if dresl == 30:
			print "Winner winner chicken dinner"
			time_as_string = str(the_timeMin) + "." + str(int(the_timeSec%60))
			time_as_float = float(time_as_string)
			print time_as_float, the_score
			print type(time_as_float)
		###########

			

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
		pygame.draw.rect(screen, (0,0,0),((screen.get_width() / 2) - 100 ,(screen.get_height() / 2) + 140,200,20), 0)
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
			elif inkey <= 127 and len(current_string) < 3:
				current_string = current_string + chr(inkey)
			self.display_box(screen, question + ": " + current_string.upper())
		return current_string.upper()