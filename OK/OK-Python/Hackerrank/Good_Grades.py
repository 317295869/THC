# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 
#

n=int(input())

if n>=0 and n<=59:
    print("F")
elif n>=60 and n<=69:
    print("D")
elif n>=70 and n<=79:
    print("C")
elif n>=80 and n<=89:
    print("B")
elif n>=90 and n<=100:
    print("A")
else:
    print("Calificacion fuera de rango")




