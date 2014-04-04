#!/usr/bin/env python
# encoding: utf-8

#---------- SKIPUN TIL AÐ VISTA Í GAGNAGRUNN
#HighScoreInsertion.insertHighscore(ident, initials, score, time)

import os, pygame, math, sys, random
from random import randrange
import math as mathh
import time as tm
from pygame import *
import menu, GUI, Deck, Card, Golf_relaxed
from Golf_relaxed import *
import HighScoreInsertion

class GUI:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((800, 500))
		pygame.display.set_caption('Gooby plz')
		pygame.mouse.set_visible(1)
		self.background = pygame.image.load("data/dolanbackground.png")
		self.backgroundRect = self.background.get_rect()
		self.font = pygame.font.Font('data/menu_font.ttf', 40)

		self.the_timeSec = 0.0
		self.the_timeMin = 0.0
		self.the_score = 0
		self.score_multiplier = 0
		self.highscore_submitted = False
		self.old_pos = None
		self.time = None
		self.game_lost = False
		self.game_won = False
		self.dragging_card = False

		self.game = Golf_relaxed()
		self.collumns = [self.game.col1.sprites(), self.game.col2.sprites(), self.game.col3.sprites(), self.game.col4.sprites(), self.game.col5.sprites(), self.game.col6.sprites(), self.game.col7.sprites()]
		self.allsprites =  pygame.sprite.LayeredUpdates((self.game.col1, self.game.col2, self.game.col3, self.game.col4, self.game.col5, self.game.col6, self.game.col7))

		clock = pygame.time.Clock()

		self.ourMenu = ["Start"]
		self.myMenu = menu.Menu(self.ourMenu, 'data/dolanbackground.png')
		self.myMenu.drawMenu()

		self.MouseLPressed = False

		while 1:
		# INPUT EVENTS
			for event in pygame.event.get():
				self.myMenu.handleEvent(event)
				# QUIT TO MENU
				if event.type == QUIT:
					return
				elif event.type == KEYDOWN and event.key == K_h:
					self.highscore_box(self.screen)
				elif event.type == KEYDOWN and event.key == K_n:
					self.new_game()
				elif event.type == KEYDOWN and event.key == K_i:
					self.instruction_box(self.screen)
				elif event.type == menu.Menu.MENUCLICKEDEVENT:
					#START AND INITIALIZE GAME
					if event.item == 0:
						isGameActive = True
						self.myMenu.deactivate()

						self.start = tm.time()
						self.set_up_collumns()
						self.set_up_deckA()
						self.set_up_deckB()
						self.selectable_collumns()
						self.add_score(0)

			if self.myMenu.isActive():
				self.myMenu.drawMenu()

			#TEIKNA HLUTI
			else:
				self.update()

				if event.type == MOUSEBUTTONDOWN:
					self.MouseLPressed = True

					#Draw from deck A
					for idx, card in enumerate(self.game.deckA.sprites()):
						if card.clicked(event.pos):
							if len(self.game.deckA.sprites()) > 0:
								self.game.deckB.add(card)
								self.game.deckA.remove(card)
								self.score_multiplier = 0
							self.add_score(50)

					#Select card from collumn
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							if card.selectable and self.dragging_card == False:
								card.clicked(event.pos)

				if event.type == MOUSEBUTTONUP:
					self.MouseLPressed = False
					last_in_deckB = self.game.deckB.sprites()[-1]

					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							if card.selected:
								card.selected = False

								#Check if card from collumn collides with the last card in Deck B
								if pygame.sprite.collide_rect(card, last_in_deckB) and (last_in_deckB.child == int(card.rank) or last_in_deckB.parent == int(card.rank)):
									self.game.deckB.add(card)	#add card to deck B
									col.pop()					#remove card from collumn
									self.selectable_collumns()	#Make last cards in collumns selectable
						
									self.score_multiplier += 1 	#Score multiplier, 
									self.add_score(100+mathh.pow(self.score_multiplier, 4))

								#For the wildcard
								elif pygame.sprite.collide_rect(card, last_in_deckB) and last_in_deckB.id == 'W21':
									self.game.deckB.add(card)	#add card to deck B
									col.pop()					#remove card from collumn
									self.selectable_collumns()	#Make last cards in collumns selectable
									self.add_score(5000)		#Increase score, 5000 points
								elif pygame.sprite.collide_rect(card, last_in_deckB) and card.id == 'W21':
									self.game.deckB.add(card)	#add card to deck B
									col.pop()					#remove card from collumn
									self.selectable_collumns()	#Make last cards in collumns selectable
								#move card to it's original position
								else:							
									card.rect.x = self.old_pos[0]
									card.rect.y = self.old_pos[1]
					#Check if we have lost the game
					if self.check_for_loss():
						self.game_lost = True
						self.fontLose = pygame.font.Font('data/menu_font.ttf', 200)
						self.textLose = self.fontLose.render("YU SUK", 1, (255,0,0))
						self.LosePos = self.textLose.get_rect()
						self.LosePos.center = (400, 250)
						for idx, col in enumerate(self.collumns):
							col[-1].selectable = False

					#Check if we have won the game and submit score and initials to database
					if self.check_for_win():
						self.game_won = True
						self.fontWinner = pygame.font.Font('data/menu_font.ttf', 150)
						self.textWinner = self.fontWinner.render("YU WON!", 1, (255, 0, 0))
						self.WinnerPos = self.textWinner.get_rect()
						self.WinnerPos.center = (415, 150)

						self.fontLose = pygame.font.Font('data/menu_font.ttf', 100)
						self.textLose = self.fontLose.render("Score: " + str(int(self.the_score)), 1, (255,0,0))
						self.LosePos = self.textLose.get_rect()
						self.LosePos.center = (400, 250)
						self.update()
						time = self.time
						if self.highscore_submitted == False:
							HighScoreInsertion.insertHighscore(randrange(10000000) , self.ask(self.screen, "Name"), str(self.the_score), time)
							self.highscore_submitted = True
							self.new_game()
							#self.new_game()

					self.dragging_card = False

					self.set_up_deckB()		#Update deck B
					self.set_up_deckA()		#Update deck A

				#Move cards from collumns
				if self.MouseLPressed == True:
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							try:
								card.move(event.pos)
								self.dragging_card = True
							except AttributeError:
								self.MouseLPressed = True

				#If card collides with mouse-pointer, we get it's coordinates.
				#So we can move it back to it's original position if the user
				#tries an invalid move
				if self.MouseLPressed == False:
					for idx, col in enumerate(self.collumns):
						for idx2, card in enumerate(col):
							if card.selectable:
								if card.rect.collidepoint(mouse.get_pos()):
									self.old_pos = (card.rect.x, card.rect.y)

			pygame.display.flip()

	#Updates cards, time and score
	def update(self):
		self.screen.blit(self.background, self.backgroundRect)
		if self.game_lost == False:
			deckA = self.game.deckA.sprites()
			deckB = self.game.deckB.sprites()
			self.allsprites.draw(self.screen)
			for idx, card in enumerate(deckA):
				card.draw(self.screen)
			for idx, card in enumerate(deckB):
				card.draw(self.screen)

			self.update_time()
			self.screen.blit(self.text, self.textpos)
			self.screen.blit(self.textTime, self.textposTime)
		if self.game_lost == True:
			self.screen.blit(self.textLose, self.LosePos)
		if self.game_won == True:
			self.screen.blit(self.background, self.backgroundRect)
			self.screen.blit(self.textLose, self.LosePos)
			self.screen.blit(self.textWinner, self.WinnerPos)
		for idx, col in enumerate(self.collumns):
			for idx2, card in enumerate(col):
				if card.selected:
					self.screen.blit(card.image,card.rect.topleft)


	#Position cards in collumns
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

	#Sets the last cards in collums selectable
	def selectable_collumns(self):
		for idx, col in enumerate(self.collumns):
			if len(col) > 0:
				col[-1].selectable = True			

	#Position cards in deck A
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
	
	#Position cards in Deck B
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

	def highscore_box(self, screen):
		f = open('highscore.txt', 'r').read().split()
		fontHigh = pygame.font.Font(None,34)
		fontobject = pygame.font.Font('data/menu_font.ttf',26)
		pygame.draw.rect(screen, (0,0,0),((screen.get_width() / 2) - 160,(screen.get_height() / 2) - 200,300,400), 0)
		pygame.draw.rect(screen, (255,255,255),((screen.get_width() / 2) - 160,(screen.get_height() / 2) - 200,300,400), 1)
		###################
		screen.blit(fontHigh.render("HISKOR", 1, (85,13,179)),((screen.get_width() / 2)-50, (screen.get_height() / 2) - 184))
		count = 0
		bil = "   "
		for i in range(len(f)-1):
			if i == 0:
				lina = f[count] + bil + f[count+1] + "  " + f[count+3] + f[count+4] + f[count+5] + "  " + f[count+2]
				screen.blit(fontobject.render(lina, 1, (255,255,255)),((screen.get_width() / 2) - 130, (screen.get_height() / 2) - 132 + count*3))
			if i % 6 == 0 and i != 0:
				count += 6
				if len(f[count]) == 3:
					bil = "  "
				lina = f[count] + bil + f[count+1] + "  " + f[count+3] + f[count+4] + f[count+5] + "  " + f[count+2]
				screen.blit(fontobject.render(lina, 1, (255,255,255)),((screen.get_width() / 2) - 130, (screen.get_height() / 2) - 132 + count*3))
		pygame.display.flip()
		while 1:
			inkey = self.get_key()
			if inkey == K_h:
				break

	def instruction_box(self, screen):
		f = open('help.txt', 'r').read().split()
		fontInstructions = pygame.font.Font(None,34)
		fontobject = pygame.font.Font('data/menu_font.ttf',26)
		pygame.draw.rect(screen, (0,0,0),((screen.get_width() / 2) - 300,(screen.get_height() / 2) - 200,600,300), 0)
		pygame.draw.rect(screen, (255,255,255),((screen.get_width() / 2) - 300,(screen.get_height() / 2) - 200,600,300), 1)
		screen.blit(fontInstructions.render("HALP", 1, (85,13,179)),((screen.get_width() / 2)-40, (screen.get_height() / 2) - 184))
		count = 0
		lina = ""
		for i in range(len(f)-1):
			if f[i] != "z":
				lina = lina + f[i] + " "
			else:
				screen.blit(fontobject.render(lina, 1, (255,255,255)),((screen.get_width() / 2) - 270, (screen.get_height() / 2) - 132 + count*3))
				lina = ""
				count += 6
		pygame.display.flip()
		while 1:
			inkey = self.get_key()
			if inkey == K_i:
				break

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

	#True if deck A is empty and there is nothing we can do
	#else False
	def check_for_loss(self):
		last_B = self.game.deckB.sprites()[-1]
		for idx, col in enumerate(self.collumns):
			for idx2, card in enumerate(col):
				if len(self.game.deckA) == 0:
					if int(last_B.rank) != 21:
						if ((len(self.collumns[0]) == 0) or (int(self.collumns[0][-1].rank) != last_B.child and int(self.collumns[0][-1].rank) != last_B.parent) and int(self.collumns[0][-1].rank) != 21):
							if ((len(self.collumns[1]) == 0) or (int(self.collumns[1][-1].rank) != last_B.child and int(self.collumns[1][-1].rank) != last_B.parent) and int(self.collumns[1][-1].rank) != 21):
								if ((len(self.collumns[2]) == 0) or (int(self.collumns[2][-1].rank) != last_B.child and int(self.collumns[2][-1].rank) != last_B.parent) and int(self.collumns[2][-1].rank) != 21):
									if ((len(self.collumns[3]) == 0) or (int(self.collumns[3][-1].rank) != last_B.child and int(self.collumns[3][-1].rank) != last_B.parent) and int(self.collumns[3][-1].rank) != 21):
										if ((len(self.collumns[4]) == 0) or (int(self.collumns[4][-1].rank) != last_B.child and int(self.collumns[4][-1].rank) != last_B.parent) and int(self.collumns[4][-1].rank) != 21):
											if ((len(self.collumns[5]) == 0) or (int(self.collumns[5][-1].rank) != last_B.child and int(self.collumns[5][-1].rank) != last_B.parent) and int(self.collumns[5][-1].rank) != 21):
												if ((len(self.collumns[6]) == 0) or (int(self.collumns[6][-1].rank) != last_B.child and int(self.collumns[6][-1].rank) != last_B.parent) and int(self.collumns[6][-1].rank) != 21):
													return True
		return False

	#True if the collumns are empty
	#else False
	def check_for_win(self):
		total_length = len(self.collumns[0]+self.collumns[1]+self.collumns[2]+self.collumns[3]+self.collumns[4]+self.collumns[5]+self.collumns[6])
		if total_length ==0:
			return True
		else:
			return False

	#Time
	def update_time(self):
		end = tm.time()
		tm.sleep(0.01)
		the_timeSec = end-self.start
		minutes = str(int(the_timeSec/60))
		seconds = str(int(the_timeSec % 60))
		if len(seconds) == 1:
			seconds = "0"+seconds
		if len(minutes) == 1:
			minutes = "0"+minutes

		self.time = minutes + " : " + seconds
		timedisp = minutes + ":" + seconds
		self.textTime = self.font.render("Time: " + timedisp, 1, (255, 255, 255))
		self.textposTime = self.textTime.get_rect()
		self.textposTime.center = (150, 475)

	#Adds a number to the score
	def add_score(self, number):
		self.the_score += number
		self.text = self.font.render("Score: %d" % (self.the_score), 1, (255, 255, 255))
		self.textpos = self.text.get_rect()
		self.textpos.center = (680, 475)

	def new_game(self):
		self.the_timeSec = 0.0
		self.the_timeMin = 0.0
		self.the_score = 0
		self.score_multiplier = 0
		self.highscore_submitted = False
		self.old_pos = None
		self.time = None
		self.game_lost = False
		self.game_won = False

		self.game = Golf_relaxed()
		self.collumns = [self.game.col1.sprites(), self.game.col2.sprites(), self.game.col3.sprites(), self.game.col4.sprites(), self.game.col5.sprites(), self.game.col6.sprites(), self.game.col7.sprites()]
		self.allsprites =  pygame.sprite.LayeredUpdates((self.game.col1, self.game.col2, self.game.col3, self.game.col4, self.game.col5, self.game.col6, self.game.col7))
		self.myMenu.activate()
