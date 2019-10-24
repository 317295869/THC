#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 22-10-2019
#
#

# Resolver el problema de los automatas celulares de primeros vecinos
# con la regla 30

import matplotlib.pyplot as plt
import numpy as np

#plt.show() 


def regla30(a,i,s):
    
    if a == 1 and i == 1 and s == 1:
        resultado = 0
    if a == 1 and i == 1 and s == 0:
        resultado = 0
    if a == 1 and i == 0 and s == 1:
        resultado = 0
    if a == 1 and i == 0 and s == 0:
        resultado = 1
    if a == 0 and i == 1 and s == 1:
        resultado = 1
    if a == 0 and i == 1 and s == 0:
        resultado = 1
    if a == 0 and i == 0 and s == 1:
        resultado = 1
    if a == 0 and i == 0 and s == 0:
        resultado = 0
    return(resultado)

n = 43
cel = [0]*n
cel[n//2] = 1

print(cel)

e = []
for i in range(n):
    e.append(regla30(cel[i-1], cel[i], cel[(i+1)%n]))
print(e)

cel = e.copy()
e = []
for j in range(22):
    e = []
    for i in range(n):
         e.append(regla30(cel[i-1], cel[i], cel[(i+1)%n]))
    cel = e.copy()
    print(cel)

Y = [21]*len(e)

plt.plot(e, Y, "sb")
plt.show()

