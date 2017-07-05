import random
import numpy as np
import matplotlib.pyplot as plt

random.seed(1) #For the sake of repeatability, the randomness is seeded, so it is the same each time.

def serie (n): 
    # n is the length of the desired serie
    # This function creates a series based on a cubic with added noise
    s=[]
    for x in range (n):
        s+=[10*(((0.05*x-2)**3)+2*((0.05*x-2)**2)+1)+random.randint(-100,100)/50]
    return s

### All teh code above is universal to all of the models    

def SMA (serie, n): 
    # n is range of the moving average
    # This function smooths a set of data points with a simple moving average
    s=[serie[0]]*(n-1)
    s=s+serie
    smoothed=[]
    for x in range (len(s)-n):
        smoothed += [np.mean(s[x:x+(n)])]
    return smoothed

series1 = serie(60) 
#This defines a serie length 60
smoothed = SMA(series1,10)
#this then smooths that series

###
plt.figure(figsize=(10,7.5))
plt.title('Simple Moving Average')
plt.legend(plot,['Actual Data','Smoothed Values'])
### cosmetic adjustments to the graph

plot = plt.plot(series1, 'r-', smoothed, 'b--')
#Plots on the same axes the original and smoothed series