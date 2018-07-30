from Deck import Deck
from Table import Table

class Game():
	"""docstring for Game"""
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()

		self.table = Table()

		for i in range(12):
			self.table.addCard(self.deck.draw())
		self.table.print()

	def begin(self):
		while not self.table.existSet():
			for i in range(3):
				self.table.addCard(self.deck.draw())

		print("How many players will be playing?")
		num_players = int(input("Enter a number greater than 0: "))

		while num_players < 1:
			num_players = input("Enter a number greater than 0: ")

		self.table.print()
		self.players_score = []
		for i in range (0, num_players):
			self.players_score.append(0)

		#for test
		print(self.players_score)

	def play(self):
		print("Who finds a set?")
		print("Please enter your player number and the cards you pick (separated by space): ")
		print("For example, player1 picks cards 1, 2 ,3 should enter 1 1 2 3 in the command line.")
		userInput = input().split()

		player = int(userInput.pop(0))

		userInput = list(map(int, userInput))
		userInput.sort()
		userInput.reverse()

		print(userInput)
		card1 = self.table.getCard(int(userInput[0]))
		card2 = self.table.getCard(int(userInput[1]))
		card3 = self.table.getCard(int(userInput[2]))

		while not self.table.isSet(card1, card2, card3):
			print("Sorry, it is not a set! Try again!")
			print("Please enter your player number and the cards you pick (separated by space): ")
			print("For example, player1 picks cards 1, 2 ,3 should enter 1 1 2 3 in the command line.")
			userInput = input().split()
			player = int(userInput.pop(0))

			userInput = list(map(int, userInput))
			userInput.sort()
			userInput.reverse()

			card1 = self.table.getCard(userInput[0])
			card2 = self.table.getCard(userInput[1])
			card3 = self.table.getCard(userInput[2])

		self.players_score[player-1] += 1
		print("Congraduations, Player%i found a set!"%(player))

		self.table.removeCard(userInput[0])
		self.table.removeCard(userInput[1])
		self.table.removeCard(userInput[2])

		for i in range(1,4):
			self.table.addCard(self.deck.draw())

		while not self.table.existSet():
			for i in range(1,4):
				self.table.addCard(self.deck.draw())

		self.table.print()

	def players_score(self):
		return self.players_score

	def finish(self):
		return self.deck.size() == 0 and not self.table.existSet()

'''
game = Game()
game.begin()
'''





