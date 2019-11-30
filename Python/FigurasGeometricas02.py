#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 10-11-19
#

print("""
Calculo de las coordenadas de un poligono regular inscrito de lado n, donde
n >= 3 && n<=12
En una circunferencia de centro C(0,0) y radio R\n\n
""")

#--------------Asignacion de radio-------------------

r=4
radio=r
print ("      Caso hipotetico de radio = %d\n"%(r))

#--------------LLamada a funciones ------------------

from math import cos
from math import sin
from math import pi
from math import radians
from math import sqrt
#import matplotlib.pyplot as plt
#import numpy as np
#from numpy import *


#---------------TRIANGULO...DODECAGONO---------------
#Funcion coordenadas de x y y

def perimetro(num_vertices,x,y):
   x1=x[0]
   y1=y[0]

   x2= x[1]
   y2=y[1]

   x=x2-x1
   y=y2-y1
   
   print("""El perimetro es %0.3f"""
   %(num_vertices*sqrt(x**2+y**2))
         )
   
def area(num_vertices,x,y):

    num_triangulos=num_vertices
    x1=x[0]
    y1=y[0]

    x2= x[1]
    y2=y[1]

    x=x2-x1
    y=y2-y1

    lado = sqrt(x**2+y**2)/2

    h=0
    k=0

    x=h-x1
    y=k-y1

    radiou=sqrt(x**2+y**2)

    apotema=sqrt(radiou**2-lado**2)

    area=lado*2*apotema*0.5*num_triangulos
    print("El area es %0.3f"%(area))

def coordenadas(angulo,num_vertices,radio):
    
   arreglo_x=list(range(num_vertices))
   arreglo_y=list(range(num_vertices))
   #arreglo_x=ones(num_vertices)
   #arreglo_y=ones(num_vertices)

   cont=1
   while cont<=num_vertices:
       x=radio*cos(cont*angulo)
       y=radio*sin(cont*angulo)
       arreglo_x[cont-1]=x
       arreglo_y[cont-1]=y
       print("Vertice %d = (%0.3f, %0.3f)"%(cont,x,y))
       cont=cont+1
   return arreglo_x, arreglo_y
        
            
print("\nLas coordenadas del triangulo inscrito son")
arreglos=coordenadas((2*pi)/3,3,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(3,arreglo_x,arreglo_y)
area(3,arreglo_x,arreglo_y)

print("\nLas coordenadas del cuadrado inscrito son")
arreglos=coordenadas((2*pi)/4,4,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(4,arreglo_x,arreglo_y)
area(4,arreglo_x,arreglo_y)

print("\nLas coordenadas del pentagono inscrito son")
arreglos=coordenadas((2*pi)/5,5,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(5,arreglo_x,arreglo_y)
area(5,arreglo_x,arreglo_y)
#print("ESPACIO")
#print(arreglo_x)
#print("ESPACIO")
#print(arreglo_y)


print("\nLas coordenadas del hexagono inscrito son")
arreglos=coordenadas((2*pi)/6,6,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(6,arreglo_x,arreglo_y)
area(6,arreglo_x,arreglo_y)

print("\nLas coordenadas del heptagono inscrito son")
arreglos=coordenadas((2*pi)/7,7,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(7,arreglo_x,arreglo_y)
area(7,arreglo_x,arreglo_y)


print("\nLas coordenadas del octagono inscrito son")
arreglos=coordenadas((2*pi)/8,8,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(8,arreglo_x,arreglo_y)
area(8,arreglo_x,arreglo_y)

print("\nLas coordenadas del eneagono inscrito son")
arreglos=coordenadas((2*pi)/9,9,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(9,arreglo_x,arreglo_y)
area(9,arreglo_x,arreglo_y)

print("\nLas coordenadas del decagono inscrito son")
arreglos=coordenadas((2*pi)/10,10,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(10,arreglo_x,arreglo_y)
area(10,arreglo_x,arreglo_y)

print("\nLas coordenadas del endecagono inscrito son")
arreglos=coordenadas((2*pi)/11,11,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(11,arreglo_x,arreglo_y)
area(11,arreglo_x,arreglo_y)

print("\nLas coordenadas del dodecagono inscrito son")
arreglos=coordenadas((2*pi)/12,12,radio)
arreglo_x=arreglos[0]
arreglo_y=arreglos[1]
perimetro(12,arreglo_x,arreglo_y)
area(12,arreglo_x,arreglo_y)

