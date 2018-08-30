'''
Created by: Tianyuan Li

The card class represents each card with an array of 4 integers, and each element in
the array represents a feature of the card.
For example: Card.new(1, 1, 1, 1) will generate a card "one red solid diamond"
'''
class Card():
	def __init__(self, number, color, shading, symbol):
		self.number = number
		self.color = color
		self.shading = shading
		self.symbol = symbol
	def toList(self):
		return [self.number, self.color, self.shading, self.symbol]
# Test the class
# card = Card(1,2,1,1)
# print(card.toList())