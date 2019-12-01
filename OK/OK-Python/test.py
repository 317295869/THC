# !/usr/bin/python3
# Eduardo Alexis Valencia Dorantes
# python 3.6.8
#
#
# 

from math import sin

x=[7,8,17,28]
y=[]

for x in range(len(x)):
    y.append(sin(x))
    print('{3}{0:2d}{3} {3}{1:3d}{3} {3}{2:4d}{3}'.format(x,x*x,x*x*x, '|'))
