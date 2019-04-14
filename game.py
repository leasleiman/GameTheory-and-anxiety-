from player import Player
import random
from math import *

class Game:

	#initialize a game with a list of players, a minimum number of player, and a probability of 
	# the most anxious player selling the stock 
	def __init__(self, players, k, prob):
		self.players = players
		self.k = k
		self.prob = prob

	#play the game
	def play(self):
		players = self.players
		#store the played players
		oldPlayers = []
		i = 1
		while len(players) > self.k:
			levels = self.getLevels(i, players)
			maxIndex = levels.index(max(levels))
			stockPrice = self.stockPrice(i)

			if random.randint(1, 10) <= (self.prob*10):
				#the most anxious player sells
				players[maxIndex].setProfit(stockPrice)
				oldPlayers += [players[maxIndex]]
				#remove the player
				players.remove(players[maxIndex])

			else:
				#choose a random player from the rest of the player
				randomPlayer = random.randint(0, (len(players)-1))
				while randomPlayer == maxIndex:
					randomPlayer = random.randint(0, (len(players)-1))
				players[randomPlayer].setProfit(stockPrice)
				oldPlayers += [players[randomPlayer]]
				players.remove(players[randomPlayer])

			i+=1
		
		self.allPlayers(players, oldPlayers)

		return oldPlayers

	def stockPrice(self, i):
		return e**i


	def getLevels(self, i, players):
		levels = []
		for player in players:
			levels = levels + [player.getAnxietyLevel(i)]
		return levels

	def allPlayers(self, remainingPlayers, players):
		for player in remainingPlayers:
			player.setProfit(0)
			players += [player]

		return players






players = [Player('x**2'), Player('x'), Player('2**x'), Player('log(x)'), Player('e**x'), Player('x**3'),
Player('x**x**x'), Player('e**(-1/x**2)')]
game = Game(players, 3, 0.6)
for p in game.play():
	print(p.getProfit())
