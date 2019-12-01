# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 
#

import math
n=int(input())

total=1000

if (n>=10 and n<=700) == True:
    yo= math.floor(n)
    amigoB= math.floor((1/3)*yo)
    amigoA= math.floor(total-(amigoB+yo))
    print(amigoA)
else:
    print("Solo puedes tomar entre 10 y 700 ml")
    

