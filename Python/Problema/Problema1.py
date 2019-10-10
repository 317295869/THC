#
# Eduardo Alexis Valencia Dorantes
# python 3.6.8
# 13-09-2019
#
#
from math import sin
# Un automóvil sube por una carretera de 3° de inclinación
# con una velocidad constante de 45 km/h. La masa del automóvil es de 1600 kg.
# Despreciar las fuerzas de fricción.
# - ¿Cuál es la potencia desarrollada por el motor?
# - ¿Cuál es el trabajo que ha efectuado en 10 s?
# Solucion: Descomponemos el peso, en la dirección a lo largo del plano
# y perpendicular al plano inclinado.
# La fuerza que ejerce el motor,
# para que el automóvil ascienda por el plano inclinado con velocidad constante:
m = 1600
g = 9.8
ang = sin(3)
F = (m*g)*ang
print(F)
# La potencia es el producto escalar de la fuerza por la velocidad de
# 45 km/h=12.5 m/s
F = (m*g)*ang
v = 12.5
P = F*v
print(P)
# El trabajo es el producto de la potencia por el tiempo,
# o de la fuerza por el desplazamiento
P = F*v
t = 10
W = P*t
print(W)

