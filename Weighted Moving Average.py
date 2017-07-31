#Weighted Moving Average

import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(0) #For the sake of repeatability, the randomness is seeded, so it is the same each time.

def serienoise (n): 
    # n is the length of the desired serie
    # This function creates a series based on a cubic with added noise
    s=[]
    for x in range (n):
        s+=[10*(((0.02*x-2)**3)+2*((0.02*x-2)**2)+1)+random.randint(-200,200)/25]
    return s
    
def serie (n): 
    # n is the length of the desired serie
    # This function creates a series based on a cubic with added noise
    s=[]
    for x in range (n):
        s+=[10*(((0.02*x-2)**3)+2*((0.02*x-2)**2)+1)]
    return s
    
def meansqrdif (serie1, serie2):
    # Determines the mean squared differnece between two series
    # takes two series as inputs and returns a float
    total=0
    for x in range (len(serie1)-1):
        total+=(serie1[x]-serie2[x])**2
    return total/len(serie1)
    
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
    
series1 = serienoise(150) 
#This defines a serie length 60 with noise included
series2 = serie(150)

smoothed = WMA(series1,30)
#this then smooths that series

###
plt.figure(figsize=(10,7.5))
plt.title('Weighted Moving Average')
plt.legend(plot,['Actual Data','Smoothed Values','True Values'])
### cosmetic adjustments to the graph

plot = plt.plot(series1, 'r-', smoothed, 'b-', series2, 'g--')
#Plots on the same axes the original and smoothed series      

print(meansqrdif(series2, smoothed))
#prints the mean squared difference of the smothed series compared to the true value
