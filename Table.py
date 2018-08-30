from Card import Card

'''
Created by: Tianyuan Li

The Table class represents the cards where players select a set from.
'''

class Table():
	"""docstring for Table"""
	def __init__(self):
		self.table = []

	def removeCard(self, index):
		self.table.pop(index)

	def addCard(self, card):
		self.table.append(card)

	def getCard(self, index):
		return self.table[index]

	def size(self):
		return len(self.table)

	def isSet(self, card1, card2, card3):
		if (card1[0]+card2[0]+card3[0]) % 3 == 0:
			if (card1[1]+card2[1]+card3[1]) % 3 == 0:
				if (card1[2]+card2[2]+card3[2]) % 3 == 0:
					if (card1[3]+card2[3]+card3[3]) % 3 == 0:
						return True
		return False

	def permutation(self):
		cardCombo = []
		allCombo = []
		for i in range(0, len(self.table)):
			for j in range(0, len(self.table)):
				for k in range(0, len(self.table)):
					if (i != j and j != k and i != k):
						cardCombo.append(self.getCard(i))
						cardCombo.append(self.getCard(j))
						cardCombo.append(self.getCard(k))
						allCombo.append(cardCombo)
						cardCombo = []
		return allCombo

	def existSet(self):
		allCombo = self.permutation()
		for cardCombo in allCombo:
			if self.isSet(cardCombo[0], cardCombo[1], cardCombo[2]):
				#for test
				print(cardCombo)
				return True
		return False

	def print(self):
		for i in range(0,len(self.table)):
			temp = "{} ==> {}".format(i, self.table[i])
			print(temp)

# Test the class
'''
table = Table()
table.addCard([1,2,3,3])
table.addCard([2,2,2,3])
table.addCard([1,3,3,1])
table.addCard([2,2,2,2])
print(table.isSet(table.getCard(0), table.getCard(1), table.getCard(2)))
print(table.size())
table.print()
print(table.existSet())
#print(table.getCard(1))
table.print()
table.removeCard(3)
print(table.existSet())
table.print()
table.removeCard(2)
print(table.existSet())
table.print()
'''
		
