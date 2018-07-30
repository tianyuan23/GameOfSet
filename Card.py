class Card():
	def __init__(self, number, color, shading, symbol):
		self.number = number
		self.color = color
		self.shading = shading
		self.symbol = symbol
	def toList(self):
		return [self.number, self.color, self.shading, self.symbol]

# card = Card(1,2,1,1)
# print(card.toList())