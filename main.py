# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 16:29:36 2019

@author: Lea
"""

from player import Player
from game import Game
import random

listOfResults=""
i=0

#Fixed it at 0.04 cause that is what they have in the paper
for i in range(5):
    player= Player(10)
    game= Game(player,0.04,1)
    game.play()
    result=game.getDelay()
    listOfResults+=str(result)+","
    i=i+1
    print(i)

currentFile= "Anxiety.txt"
fileOut= open( currentFile, "w")
line1=listOfResults
fileOut.write(line1)
fileOut.close()

k=input("Program ends here.")
