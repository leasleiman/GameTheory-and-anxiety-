# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:53:11 2019

@author: Lea
"""

'''
Player class represents a player with given anxiety function
'''
from math import exp, sqrt
import random

#HAMR=
class Player:

    #create a player with given function which is a string
    #HAMR=Hamilton Anxiety Rating Scale
    def __init__(self, willToWin, fundValue):
        self.profit = 0
        self.signal=False
        self.fundValue= fundValue
        self.anxiety=1
        self.HAMR=0
        self.willToWin=willToWin

    #get the anxiety level with given time
    def getAnxietyLevel(self):
        return self.anxiety

    #set the profit 
    def setProfit(self, profit):
        self.profit = profit

    #get the profit
    def getProfit(self):
        return self.profit

    #set the signal 
    def setSignal(self,boolSignal):
        self.signal= boolSignal

    #get the fundamental value we set 
    def getValue(self):
        return self.fundValue
    
    def getHAMR(self):
            return self.HAMR

    def startAnxiety(self,anxTime):
        anxiety= sqrt(exp(anxTime-self.willToWin))
       
        if (abs(anxiety-self.anxiety>=10)):
            self.HAMR +=4
      
        elif (abs(anxiety-self.anxiety>=5)):
            self.HAMR += 3

        elif (abs(anxiety-self.anxiety>=3)):
            self.HAMR+=2

        self.anxiety=anxiety
                
