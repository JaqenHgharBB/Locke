#Kalman Filter

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

def kalman(sys,z,x_prev,p_prev):
    #performs the kalman filter, taking as inputs the system variables, the measurement, and the previous data
    #returns as outputs the new estimate and the new error covariance
    x_pred=sys[0]*x_prev
    p_pred=sys[0]*p_prev*np.transpose(sys[0])+sys[2]
    K=(p_pred*np.transpose(sys[1]))*np.linalg.pinv((sys[1]*p_pred*np.transpose(sys[1]))+sys[3])
    x_new=x_pred+K*(z-sys[1]*x_pred)
    p_new=p_pred-K*sys[1]*p_pred
    return [x_new,p_new]

def kfilter (x,p,sys, data):
    # loops the filter across a dataset
    z=data[0]
    i=kalman(sys,z,x,p)
    #runs the filter once and puts the results in a varibale that the repeating loop can then use
    k=[]
    p=[]
    for l in range (len(data)):
        z=data[l]
        i=kalman(sys,z,i[0],i[1])
        k+=[np.squeeze(np.asarray(i))[0][0][0]]
        # squeezing the array version of the matrices allows for integer, rather than matrix, outputs
        # if the data being treated were non-scalar, these would have to be removed
    return k

def KF (serie):
    a=np.matrix('1,0;0,1')
    h=np.matrix('1.0,0;0,1.0')
    q=np.matrix('0.1,0;0,0.1') 
    r=np.matrix('0.9,0;0,0.9')
    sys=(a,h,q,r)
    smoothed = kfilter(serie[0],1,sys,serie)
    return smoothed

series1 = serienoise(60) 
#This defines a serie length 60 with noise included
series2 = serie(60)

smoothed = KF(series1)
#this then smooths that series

###
plt.figure(figsize=(10,7.5))
plt.title('Kalman Filter')
plt.legend(plot,['Actual Data','Smoothed Values','True Values'])
### cosmetic adjustments to the graph

plot = plt.plot(series1, 'r-', smoothed, 'b-', series2, 'g--')
#Plots on the same axes the original and smoothed series      
