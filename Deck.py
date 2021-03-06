import random
from Card import Card

'''
Created by: Tianyuan Li

The Deck class generates a deck with 81 cards.
'''

class Deck():
	"""docstring for Deck"""
	def __init__(self):
		self.deck = []
		for number in range(1,4):
			for color in range(1,4):
				for shading in range(1,4):
					for symbol in range(1,4):
						self.deck.append(Card(number, color, shading, symbol).toList())
	
	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self):
		return self.deck.pop()
		
	def size(self):
		return len(self.deck)

	def toList(self):
		return self.deck
# Test the class
# deck = Deck()
# print(deck.size())
		
			