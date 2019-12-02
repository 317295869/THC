#!/usr/bin/python3.7
#
# Valencia Dorantes Eduardo Alexis
# Python 3.6.8
#
#
#

def toplel(r):
    if 1<=amount<6:
        return("Patient has bright red face")
    if 5<amount<13:
        return("Patient is unable to speak")
    if 12<amount<21:
        return("Patient's sides are mildly bruised")
    if 20<amount<31:
        return("Patient has broken jaw, fractured ribs")
    if 30<amount<50:
        return("Patient is in a coma")
    if amount>=50:
        return("Patient is dead")
    
n=input()

lol=n.count('lol')
lel=4*(n.count('lel'))
lmao=3*(n.count('lmao'))
rofl=2*(n.count('rofl'))

amount=lol + lel + lmao + rofl

print(toplel(amount))
