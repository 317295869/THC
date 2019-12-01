# !/usr/bin/python3
# Eduardo Alexis Valencia Dorantes
# python 3.6.8
#
#
# 



def sumaI(n):
    """
"""
    r = 0
    for i in range(n+1):
        r+= 1
    return(r)

def sumaG(n):
    """
"""
    return( n*(n+1) )/2

def sumaR(n):
    """
"""
    if (n==1):
        return(1)
    else:
        return( n + sumaR(n-1) )

print(sumaI(5))
print(sumaG(5))
print(sumaR(5))
