#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 19/09/2019 25/09/2019
#
#

#plt.show()
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
print("Triangulo equlatero de lado 2, en el cuadrante I")
print("Con un vertice en el origen")

tax = 0
tay = 0

tbx = tax+2
tby = 0

pmx = (tax+tbx)/2
cateto = 2**2 - pmx**2
cateto = sqrt(cateto)

tcx = pmx
tcy = cateto

x = np.array([tax,tbx,tcx,tax])
y = np.array([tay,tby,tcy,tay])

print("""
Las coordenadas son:
A = (%d, %d)
B = (%d, %d)
C = (%d, %0.2f)
"""%(tax, tay, tbx, tby, tcx, tcy))

ax=plt.gca()
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('center')

plt.gca().set_aspect('equal',adjustable='box')
plt.plot(x, y, label='linear',color='r')


print("Cuadrado en el cuadrante I, de lado 2")
print("con un vertice en el origen")

cax = 0
cay = 0

cbx = cax+2
cby = 0

ccx = 0
ccy = cay+2

cdx = cax+2
cdy = cay+2

x = np.array([cax,cbx,cdx,ccx,cax])
y = np.array([cay,cby,cdy,ccy,cay])

print("""
Las coordenadas son:
A = (%d, %d)
B = (%d, %d)
C = (%d, %d)
D = (%d, %d)
"""%(cax, cay, cbx, cby, ccx, ccy, cdx, cdy))

ax=plt.gca()
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('center')

plt.gca().set_aspect('equal',adjustable='box')
plt.plot(x, y, label='linear',color='r')

print("Rectangulo en el cuadrante I, de altura 2 y base 6")
print("con un vertice en el origen")

rax = 0
ray = 0

rbx = rax+6
rby = 0

rcx = 0
rcy = ray+2

rdx = rax+6
rdy = ray+2

x = np.array([rax,rbx,rdx,rcx,rax])
y = np.array([ray,rby,rdy,rcy,ray])

print("""
Las coordenadas son:
A = (%d, %d)
B = (%d, %d)
C = (%d, %d)
D = (%d, %d)
"""%(rax, ray, rbx, rby, rcx, rcy, rdx, rdy))

ax=plt.gca()
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('center')

plt.gca().set_aspect('equal',adjustable='box')
plt.plot(x, y, label='linear',color='r')

print("Paralegramo ubicado en el cuadrabte I con un vertice en origen")
print("de lado 2 y altura 2, inclinado a 45° respecto al origen")

pax = 0
pay = 0

pbx = pax+2
pby = pay

pcx = sqrt(2+2)
pcy = pcx

pdx = pcy+2
pdy = pcy

x = np.array([pax,pbx,pdx,pcx,pax])
y = np.array([pay,pby,pdy,pcy,pay])

print("""
Las coordenadas son:
A = (%d, %d)
B = (%d, %d)
C = (%d, %d)
D = (%d, %d)
"""%(pax, pay, pbx, pby, pcx, pcy, pdx, pdy))

ax=plt.gca()
ax.spines['right'].set_position('center')
ax.spines['top'].set_position('center')

plt.gca().set_aspect('equal',adjustable='box')
plt.plot(x, y, label='linear',color='r')

plt.legend()
plt.show()
