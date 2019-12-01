# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 
#


from datetime import datetime, timedelta
from math import sin, cos, pi


def celciusAfahrenheit(c):
    Celsius = int(raw_input("Enter a temperature in Celsius: "))

    Fahrenheit = 9.0/5.0 * Celsius + 32

    print ("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")
    return(resultado)


def fahrenheitAcelcius(f):
    Fahrenheit = int(raw_input("Enter a temperature in Fahrenheit: "))

    Celsius = (Fahrenheit - 32) * 5.0/9.0

    print ("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")
    return(resultado)

def tiempo_1(v,y):
    t1 = (-v + math.sqrt(v**2-4*(-4.9)*y))/(-9.8)
    return (t1)
def tiempo_2(v,y):
    t2 = (-v - math.sqrt(v**2-4*(-4.9)*y))/(-9.8)
    return (t2)

def segaaños():
    sec = timedelta(seconds=int(input('Enter the number of seconds: ')))
    d = datetime(1,1,1) + sec

    print("DAYS:HOURS:MIN:SEC")
    print("%d:%d:%d:%d" % (d.day-1, d.hour, d.minute, d.second))
    return(resultado)

def añosaseg():
    t = "Fecha actual"
    fn = "Fecha de nacimeinto"
    años = (t-datetime.datetime(fn,1,1)).total_seconds()
    print(años)
    return(resultado)

def main():
    print ("Convierte medidas inglesas a sistema metrico")
    millas = input("Cuántas millas?: ")
    pies = input("Y cuántos pies?: ")
    pulgadas = input("Y cuántas pulgadas?: ")

    metros = 1609.344 * millas + 0.3048 * pies + 0.0254 * pulgadas
    print ("La longitud es de ", metros, " metros")



# programa 1
x = pi/4
val = sin(x)**2 + cos(x)**2
print (val)

# programa 2
A = '3'
B = '2'
C = A + B
print (C)


'''

    Recuerden:

/  es la division flotante
// es la division entera
%  es el modulo

no olviden dejar un espacio cuando utilicen
los operadores aritmeticos +, - y con el
de asignacion =

no utilicen espacios cuando utilicen los
operadores *, / y **


un igual es asignacion, dos iguales son comparacion
.git es el directorio con el que no hay que "meterse"

y finalmente:
"los peces son amigos, no comida"
(bueno esta no creo que sea muy util pero me acorde :) )

'''


