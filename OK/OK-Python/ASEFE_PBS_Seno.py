# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 07-11-19
#

# Evaluacion 07 11 2019

from math import cos
from math import sin
from math import sqrt
from math import pi


def seno(alpha):
    beta=alpha/pow(2,5)
    print("""
   Aproximación al seno de %f con B = %0.4f/2^5     

          Iteracion        Sin(2B)            

    """%(alpha,alpha))
    
    for i in list(range(5)):
        coseno_angulo=sqrt(1-pow(beta,2))
        seno_doble=2*beta*coseno_angulo
        beta=seno_doble
        print("""             %d             %0.7f   """%(i+1,beta))
    print("""\n   El valor de sin(%0.4f) = %0.7f aprox= Sin(2B)"""%(alpha,beta))
    print("""---------------------------------------------------------""")

lista=[0.1,0.5,1.5,pi]

for valor in lista:
    seno(valor)
    

