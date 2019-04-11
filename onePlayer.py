from player import Player
import random
from math import *

class OnePlayer:

	def __init__(self, player):
		self.player = player

	def play(self):
		prob = 0.5
		i = 1
		while True:
			if self.player.getSignal(): #stock price exceeds the value
				if random.randint(1, 100) <= (prob*100):
					self.player.setProfit(self.stockPrice(i))
					return i
				else:
					prob += 0.1

			else: #stock price hasn't exceed the value yet
				if self.stockPrice(i) > self.player.getValue():
					player.setSignal()
			i+=1



	def stockPrice(self, i):
		return e**i

player = Player(50)
game = OnePlayer(player)
print(game.play())