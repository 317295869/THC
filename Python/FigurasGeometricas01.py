#
# Eduardo Alexis Valencia Dorantes
# python 3.5.3
# 17/09/2019
#
#
print("""
Calculo de las coordenadas de un poligono regular inscrito de lado n, donde
n >= 3 && n<=12
En una circunferencia de centro C(0,0) y radio R\n\n
""")

#---------------------------------------

#Asignacion de radio

r=4
radio=r
print (" Caso hipotetico de radio = %d\n"%(r))

#--------------TRIANGULO ----------------

from math import cos
from math import sin
from math import pi
from math import radians

ax=0
ay=r

bx= -r*cos(radians(30))
by= -r/2

cx= r*cos(radians(30))
cy= -r/2

print("""
Las coordenadas del triangulo inscrito son
A(%0.3f, %0.3f)
B(%0.3f, %0.3f)
C(%0.3f, %0.3f)
"""%(ax, ay, bx, by, cx, cy))

#-------------CUADRADO ------------------

ax= -r*cos(radians(45))
ay= r*sin(radians(45))

bx= -r*cos(radians(45))
by= -r*sin(radians(45))

cx= r*cos(radians(45))
cy= -r*sin(radians(45))

dx= r*cos(radians(45))
dy= r*sin(radians(45))

print("""
Las coordenadas del cuadrado inscrito son
A(%0.3f, %0.3f)
B(%0.3f, %0.3f)
C(%0.3f, %0.3f)
D(%0.3f, %0.3f)
"""%(ax, ay, bx, by, cx, cy, dx, dy))

#---------------PENTAGONO...DODECAGONO-------------------
#Funcion coordenadas de x y y

def coordenadas(angulo,num_vertices,radio):
   from math import cos
   from math import sin

   cont=1
   while cont<=num_vertices:
       x=radio*cos(cont*angulo)
       y=radio*sin(cont*angulo)
       print("Vertice %d = (%0.3f, %0.3f)"%(cont,x,y))
       cont=cont+1

print("Las coordenadas del pentagono inscrito son")
coordenadas((2*pi)/5,5,radio)

print("\nLas coordenadas del hexagono inscrito son")
coordenadas((2*pi)/6,6,radio)

print("\nLas coordenadas del heptagono inscrito son")
coordenadas((2*pi)/7,7,radio)

print("\nLas coordenadas del octagono inscrito son")
coordenadas((2*pi)/8,8,radio)

print("\nLas coordenadas del nonagono inscrito son")
coordenadas((2*pi)/9,9,radio)

print("\nLas coordenadas del decagono inscrito son")
coordenadas((2*pi)/10,10,radio)

print("\nLas coordenadas del undecagono inscrito son")
coordenadas((2*pi)/11,11,radio)

print("\nLas coordenadas del dodecagono inscrito son")
coordenadas((2*pi)/12,12,radio)



