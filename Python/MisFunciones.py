# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 10-11-19
#

#Funciones definidas por el usuario

num1=-5
num2=3
num3=-2
num4=-15
num5=20

num6=7.89999
num7=1.22
num8=3.5

def vabs(x):
 
   if x >= 0:
       return(x) 
   else:
        valor_absoluto = x*(-1)
        return(valor_absoluto) 

absoluto=vabs(num1)
print("El valor absoluto de %d es %d"%(num1,absoluto))


def signo(x):

    if x>0:
        return (1)
    if x < 0:
        return (-1)
    if x==0:
        return (0)

signo= signo(num1)
print("El signo de %d es %d"%(num1,signo))


def multiplica(a,b):
    c=a*b
    return(c)

resultado=multiplica(num1,num2)
print("La multiplicacion de %d por %d es %d"%(num1,num2,resultado))

def elMayor(a,b):
    if a>=b:
      return(a)
    else:
      return(b)

comparacion=elMayor(num2,num3)
print("El numero mayor entre %d y %d es %d"%(num2,num3,comparacion))

def elMenor(a,b):
    if a<=b:
        return(a)
    else:
      return(b)

comparacion=elMenor(num3,num4)
print("El numero menor entre %d y %d es %d"%(num3,num4,comparacion))

def rectangular(x):
    
    if vabs(x)>0.5:
        return(0)
    if vabs(x)==0.5:
        return(0.5)
    if vabs(x)<0.5:
        return(1)

print("""
La funcion definida como:
Regresa 0   si |x| > 1/2
Regresa 1/2 si |x| = 1/2
Regresa 1   si |x| < 1/2
Si el valor de x=%d, entonces la funcion regresa %d
"""
%(num3, rectangular(num3))
      )

def identidad(x):
    return(x)

print("La identidad de %d es %d"%(num2,identidad(num2)))

def rampa(x):
    if x<0:
        return (0)
    if x >= 0:
        return (x)

print(
"""
Regresa 0 si x < 0
Regresa x si x >= 0
Si el valor de x=%d, entonces la funcion regresa %d
"""
%(num5,rampa(num5))
    )

def parte_entera(x):
    a=int(x)
    return(a)
print("La parte entera de %f es %d"%(num6,parte_entera(num6)))
    
def enteroMayor(x):
    import math
    return(math.ceil(x))
print("El entero mayor de %f es %d"%(num8,enteroMayor(num8)))

def enteroMenor(x):
    import math
    return(math.floor(x))
print("El entero menor de %f es %d"%(num7,enteroMenor(num7)))

def parte_fraccionaria(x):
    return(x-enteroMenor(x))
print("La parte fraccionaria de %f es %f"%(num6,parte_fraccionaria(num6)))

def ulam(n):
    if n%2 == 0:
        return(n/2)
    else:
        return(3*n+1)
print("""
Si el numero es par, lo divide entre 2
Si el numero es impar, lo multiplica por 3 y le suma 1
Para el numero %d, entonces %d
      """
%(num2,ulam(num2))
      )

## areas y perimetros de las figuras inscritas
## 
