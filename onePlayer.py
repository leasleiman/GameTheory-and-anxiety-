from player import Player
import random
from math import *

class OnePlayer:

	def __init__(self, player):
		self.player = player

	def play(self,prob):		
		i = 1
		while True:
			thisProb = sqrt(self.player.getAnxietyLevel(i))*prob
			print(thisProb)
			if self.player.getSignal(): #stock price exceeds the value
				if random.randint(1, 100) <= thisProb:
					self.player.setProfit(self.stockPrice(i))
					return i

			else: #stock price hasn't exceed the value yet
				if self.stockPrice(i) > self.player.getValue():
					player.setSignal()
			i+=1



	def stockPrice(self, i):
		return e**(0.25*i)

print('start')
player = Player('x**3', 50)
game = OnePlayer(player)
print(game.play(0.5))