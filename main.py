from Game import Game

if __name__=="__main__":
	game = Game()
	game.begin()
	while not game.finish():
		game.play()

	print("Game over!")