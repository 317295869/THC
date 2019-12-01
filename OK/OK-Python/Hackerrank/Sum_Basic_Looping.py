# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 
#

n=int(input())

if n>=1 and n<=100:
    suma=0
    for i in list(range(n)):
        i=i+1
        suma=suma+i
    print(suma)
else:
    print("Sumas menores de 100 terminos")




