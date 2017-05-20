# -*- coding: utf-8 -*-
"""
Created on Sat May 20 11:54:20 2017

@author: Aditya
"""

import numpy as np

'''
Read data from files
'''

fx = open('ex2x.dat', 'r')
x = []
for line in fx:
    item = line.rstrip()
    x.append(item)

x = np.array(x, dtype=float)

fx.close()

fy = open('ex2y.dat', 'r')
y = []
for line in fy:
    item = line.rstrip()
    y.append(item)

y = np.array(y, dtype=float)

fy.close()

m = len(y)

'''
Set learning rate and number of iterations
'''

alpha = 0.07
iters = 1500

'''
Gradient Descent Method
'''

z = np.ones((x.shape[0], 2))
z[:,0] = x
x = z

theta = np.zeros((2,1))

for i in range(iters):
    predictions = np.dot(x, theta).flatten()
    k = predictions - y
    theta[0,0] = theta[0,0] - alpha * (1./m) * np.sum(k*x[:,0])  
    theta[1,0] = theta[1,0] - alpha * (1./m) * np.sum(k*x[:,1])    
    
'''
Result
'''
print(theta)
    
