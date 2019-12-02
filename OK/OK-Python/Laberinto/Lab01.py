#!/usr/bin/python3.7
#
# Valencia Dorantes Eduardo Alexis
# Python 3.6.8
#
#
#

def cargarlaberinto(laberinto):
    archivo=open("LEduardo.txt","r")
    l1=" "
    l=[]
    while l1:
        l1=archivo.readline()
        if l1:
            l1=l1.rstrip()
            l1=[int(x) for x in list(l1)]
            l.append(l1)
    return(l)
l=cargarlaberinto("LEduardo.txt")
print(l)
