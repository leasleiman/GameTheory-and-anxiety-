'''
Player class represents a player with given anxiety function
'''
from math import *

class Player:

	#create a player with given function which is a string
	def __init__(self, function):
		self.function = function

	#get the anxiety level with given time
	def getAnxietyLevel(self, x):
		func = self.function.replace('x', str(x))
		return eval(func)







