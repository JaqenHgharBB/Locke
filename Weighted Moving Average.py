#Weighted Moving Average

import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(1) #For the sake of repeatability, the randomness is seeded, so it is the same each time.

def serienoise (n): 
    # n is the length of the desired serie
    # This function creates a series based on a cubic with added noise
    s=[]
    for x in range (n):
        s+=[10*(((0.05*x-2)**3)+2*((0.05*x-2)**2)+1)+random.randint(-100,100)/50]
    return s
    
def serie (n): 
    # n is the length of the desired serie
    # This function creates a series based on a cubic with added noise
    s=[]
    for x in range (n):
        s+=[10*(((0.05*x-2)**3)+2*((0.05*x-2)**2)+1)]
    return s
    
### All the code above is universal to all of the models 

def WMA (serie, n): 
    # n is range of the moving average
    # This function smooths a set of data points with a weighted moving average
    s=[serie[0]]*(n-1)
    s=s+serie
    smoothed=[]
    for x in range (len(s)-n):
        smoothrange=s[x:x+n]
        smooth = 0
        for y in range (n):
            smooth += (y+1)*smoothrange[y]
        smoothed+=[smooth/(0.5*n*(n+1))]
    return smoothed
    
series1 = serienoise(60) 
#This defines a serie length 60 with noise included
series2 = serie(60)

smoothed = WMA(series1,10)
#this then smooths that series

###
plt.figure(figsize=(10,7.5))
plt.title('Weighted Moving Average')
plt.legend(plot,['Actual Data','Smoothed Values','True Values'])
### cosmetic adjustments to the graph

plot = plt.plot(series1, 'r-', smoothed, 'b-', series2, 'g--')
#Plots on the same axes the original and smoothed series