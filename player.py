'''
Player class represents a player with given anxiety function
'''
from math import *

class Player:

	#create a player with given function which is a string 
	def __init__(self, value):
		#self.function = function
		self.value = value
		self.profit = 0
		self.isSignaled = False

	#get the anxiety level with given time
	def getAnxietyLevel(self, x):
		func = self.function.replace('x', str(x))
		return eval(func)

	#set the profit 
	def setProfit(self, profit):
		self.profit = profit

	#get the profit
	def getProfit(self):
		return self.profit

	def getValue(self):
		return self.value

	def setSignal(self):
		self.isSignaled = True

	def getSignal(self):
		return self.isSignaled


