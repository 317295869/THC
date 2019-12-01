# !/usr/bin/python3
# Eduardo Alexis Valencia Dorantes
# python 3.6.8
#
#
# Fractal de Cantor

import matplotlib.pyplot as plt
import numpy as np

#plt.show() 

l = ([0,1])
print(l)
def div (a,b):
	c=(b-a)/3
	return([a,a+c], [a+2*c,b])

ne= div(0, 1)
print(ne)
"""
nl = []
for elemento in ne:
    [r1, r2]= div(elemento[0], elemento[1])
    #print(r1)
    #print(r2)
    nl.append(r1)
    nl.append(r2)
print(nl)
"""

#print(div(0,30))
#print(ne)
#[c, d]= div(0, 1)
#print(c)
#print(d)
#div(0, c)
#print(div(0, c))
#div(d, 31)
#print(div(d,30))
#print(div(0,c),div(d,1))
#ne= div(0, 1)
#print(ne)
for i in range(5):
    #ne= nl.copy()
    nl = []
    for elemento in ne:
        [r1, r2]= div(elemento[0], elemento[1])
        #print(r1)
        #print(r2)
        nl.append(r1)
        nl.append(r2)
    ne = nl.copy()
print(nl)
