# !/usr/bin/python3
# Eduardo Alexis Valencia Dorantes
# python 3.6.8
#
#
#

#\lstinputlisting[language=Python]{/tmp/Seno.py}
from math import fabs

def raizR(b,h,x,e,i):
    if fabs(b-h)> e:
        print(b,h)
        return(raizR((b+h)/2,x/((b+h)/2),x,e,i+1))
    else:
        print("fin")
        return [b,i]

def raiz(x):
    return(raizR(x,1,x,0.00000001,0))

print(raizR(9,1,9,.00001,0))
print(raiz(9))
[r, y] = raiz(9)
print(r)
print(y)
