# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:53:21 2019

@author: Lea
"""

from player import Player
import time
from math import exp
import random

class Game:

        #initialize a game with a player, a rate of stcok growth, and the initial value of the stock
        def __init__(self, player, rate, initValue):
            self.player=player
            self.rate=rate
            self.initValue=initValue
            self.delayTime=0
            self.initTime=0

        def stockPrice(self):
            valueFunction= exp(self.rate)
            self.initValue=valueFunction
        
        def setinitTime(self,time):
            self.initTime=time

        def getStockValue(self):
            return self.initValue
       
        #delay is defined as the time period between when the signal is sent and the player sells the stock
        def getDelay(self):
            return self.delayTime
        
       #Starts the game
        def play(self):
            self.setinitTime(time.time())
            self.player.startAnxiety(1+time.time()-self.initTime)

            time.sleep(random.randint(1,4))
            while(self.getStockValue()< self.player.getValue()):

                self.player.startAnxiety(time.time()-self.initTime)
                time.sleep(random.randint(1,4))
                    
                if(self.player.getHAMR() >=25):
                    self.delayTime=0
                    return
              
                else:
                    self.player.startAnxiety(time.time()-self.initTime)
                    time.sleep(random.randint(1,4))
                    self.stockPrice()
                                
                self.player.startAnxiety(time.time()-self.initTime)    
                time.sleep(random.randint(1,4))
                
                self.player.setSignal(True)
                startDelay= time.time()
        
                while (self.player.getHAMR()<= 25):
                    self.player.startAnxiety(time.time()-self.initTime)
                    time.sleep(random.randint(1,4))

                endDelay=time.time()
                delayTime= endDelay-startDelay
                self.player.setProfit(self.getStockValue())
                
                self.delayTime=delayTime
                return 

