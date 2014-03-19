#!/usr/bin/env python
# encoding: utf-8

import random
import time
from itertools import chain

class Deck:
	def __init__(self):
		self.deck = []
		self.create_shuffled_deck()

	def __str__(self):
		return self.deck.deck

	#N: self.Deck = self.createDeck()
	#F: Ekkert
	#E: Buid er ad bua til spilastokk med 52 spilum
	def create_shuffled_deck(self):
		suit = ['H', 'L', 'S', 'T']
		rank = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
		for s in suit:
			for r in rank:
				self.deck.append(s+`r`)
		random.shuffle(self.deck)
		return self.deck

	#N: self.deck.isEmpty()
	#F: self.deck er spilabúnki
	#E: True ef búnkinn er ekki tómur, annars False
	def isEmpty(self):
		if(len(self.deck) == 0):
			return True
		else:
			return False

	#N: self.deck.draw_card()
	#F: self.deck er búnki með spilum
	#E: Búið er að draga aftasta spilið úr búnkanum
	def draw_card(self):
		if not self.isEmpty():
			return self.deck.pop()

class Deck_B:
	def __init__(self):
		self.deck_b = []

	def __str__(self):
		return self.deck_b


class Table:
	def __init__(self):
		self.table = [[0,0,0,0,0] for collumn in range (7)]

	def __str__(self):
		result = "\n".join("\t".join(map(str,l)) for l in self.table)
		return result

class Game:
	def __init__(self):
		self.deck_a = Deck()
		self.deck_b = Deck_B()
		self.table = Table()
		self.set_up_game()

	#N: self.set_up_game()
	#F: Ekkert
	#E: Ef Búnki A var ekki tómur, þá er búið að stilla upp leiknum.l
	#	Þ.e. búa til 7 dálka með 5 spilum hvor, búnka A sem inniheldur
	#	afgangs spilin og búnka B sem inniheldur eitt dregið spil úr A.
	#	Annars eitthvað ???
	def set_up_game(self):
		if(not self.deck_a.isEmpty()):
			for col_index, collumn in enumerate(self.table.table):
				for slot in range(0,5):
					collumn[slot] = self.deck_a.draw_card()
				self.deck_b = self.deck_a.draw_card()

	#N: self.begin_time()
	#F: Ekkert
	#E: Búið er að setja á stað tímateljara
	def begin_time(self):
		start = time.time()
		while (True):
			end = time.time()
			time.sleep(0.01)
			timi = "%.3f" % (end-start)

	#N: self.reset_game()
	#F: Ekkert
	#E: Búið er að frumstilla leikinn.
	def new_game(self):
		self.__init__()


def main():
	game = Game()

if __name__ == '__main__':
    main()