#!/usr/bin/python3.7
#
# Eduardo Alexis Valencia Dorantes 
# Python 3.6.8
#
#
#

x = int(input())
y = int(input())
z = int(input())
n = int(input())


print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
