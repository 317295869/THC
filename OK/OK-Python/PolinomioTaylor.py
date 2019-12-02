# !/usr/bin/python3
# Eduardo Alexis Valencia Dorantes
# python 3.6.8
#
#
#


import math
 
x = float(input("Ingrese x: "))
 
exp = 1
senox = 0
comparacion = 1
i = 1
 
while math.fabs(comparacion - senox) > 0.001:
 
    comparacion = senox
 
    if i % 2 == 0:
 
        senox -= (x**exp) / math.factorial(exp)
 
    else:
 
        senox += (x**exp) / math.factorial(exp)
 
    exp += 2
    i += 1
 
print ("ANS:",senox)
