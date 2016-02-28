# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:58:31 2016

Markov Chain Monte Carol ( or something like that, MCMC)

@author: katar
"""
import numpy
import random
"""
Concept: 1) define a markov chain
         2) run a monte carlo simulation using the 
            markov chain to 

"""

stateNames =['tropics','city','mountains']


""" the value of a process at time period t """
class State:
    def __init__(self,stringname):#,timest):
        self.name = stringname
        #self.numvisits = 0
        self.here = 0
        #self.time = timestep
        #self.idnum = 0
    
    #def visited(self):
        #self.numvisits += 1
    
    def currentState(self):
        self.here = 1
        
    def leftState(self):
        self.here = 0

# All states!
class ArrayStates:
    def __init__(self,stateNames=[]):
        self.stateSet = set()
        self.listOfStates = stateNames
        self.stateLocations = []
    
    def initialAddStates(self):
        for state in range(len(stateNames)):
            self.stateSet.add(stateNames[state])
            #self.listOfStates.append(stateNames[state])
            self.stateLocations.append(State(stateNames[state]))
    
    def length(self):
        return len(self.listOfStates)
        
    def addState(self,additionalStateName):
        self.stateSet.add(additionalStateName)
        self.listOfStates.append(additionalStateName)
        self.stateLocations.append(State(additionalStateName))

""" one step transition probability matrix between states"""
transMatrix = numpy.matrix('0 0.7 0.3; 0.5 0 0.5; 0.7 0.2 0.1')

""" numpy.matrix[i] to array """
def Matrix1dToArray(npmatrix):
    matrix1d = numpy.asarray(npmatrix)[0]   
    return matrix1d

""" chose state based """
def nextState(currentIndex, transMatrix):
    transProbs = transMatrix[currentIndex]
    sortedProbs = transProbs.sort()
    sortIndices = transProbs.argsort()
    #sums = [for]
    rand = random.random()
    

""" take n steps in the Markov chain"""
#def nSteps(n, ArrayOfStates, transMatrix):
    #initState = randint(0,ArrayOfStates.length()-1)
    #for i in range(n):
        



""" Example Markov Chain! 

    It's having ArrayStates, and defining the  probabilities between
    each of the states with the transMatrix! Then, the prob. of 
    being in some state next has to do with which state you are in
    now,

"""   
example = ArrayStates(stateNames)
example.initialAddStates()


