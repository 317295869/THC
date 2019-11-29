# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 19/09/2019 25/09/2019
#
#

# Se debe calcular el área de las figuras inscritas en un círculo de radio igual a 2
# tal que el centro de cada figura sea concentrico
# Las figuras son un: triángulo, cuadrado, pentagono, hexagono, n-agono.

#plt.show()

from math import *
import matplotlib.pyplot as plt
import numpy as np

# Triángulo

r = 2
L = 3
a = 2*pi/L

tax = r*cos(a)
tay = r*sin(a)

tbx = r*cos(2*a)
tby = r*sin(2*a)

tcx = r*cos(3*a)
tcy = r*sin(3*a)

x = np.array([tax,tbx,tcx,tax])
y = np.array([tay,tby,tcy,tay])

print("""Las coordenadas para el triángulo inscrito
en una circunferencia de radio 2 son:
A = (%5d, %5.2f)
B = (%5d, %5.2f)
C = (%5d, %5d)"""%(tax, tay, tbx, tby, tcx, tcy))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Cuadrado

S = 4
f = 2*pi/S

cax = r*cos(f)
cay = r*sin(f)

cbx = r*cos(2*f)
cby = r*sin(2*f)

ccx = r*cos(3*f)
ccy = r*sin(3*f)

cdx = r*cos(4*f)
cdy = r*sin(4*f)

x = np.array([cax,cbx,ccx,cdx,cax])
y = np.array([cay,cby,ccy,cdy,cay])

print("""Las coordenadas para el cuadrado inscrito
en una circunferencia de radio 2 son:
A = (%5d, %5d)
B = (%5d, %5d)
C = (%5d, %5d)
D = (%5d, %5d)"""%(cax, cay, cbx, cby, ccx, ccy, cdx, cdy))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='y')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Pentagono

K = 5
q = 2*pi/K

pax = r*cos(q)
pay = r*sin(q)

pbx = r*cos(2*q)
pby = r*sin(2*q)

pcx = r*cos(3*q)
pcy = r*sin(3*q)

pdx = r*cos(4*q)
pdy = r*sin(4*q)

pex = r*cos(5*q)
pey = r*sin(5*q)

x = np.array([pax,pbx,pcx,pdx,pex,pax])
y = np.array([pay,pby,pcy,pdy,pey,pay])

print("""Las coordenadas para el pentagono inscrito
en una circunferencia de radio 2 son:
A = (%5d, %5d)
B = (%5d, %5d)
C = (%5d, %5d)
D = (%5d, %5d)
E = (%5d, %5d)"""%(pax, pay, pbx, pby, pcx, pcy, pdx, pdy, pex, pey))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='c')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Hexagono

D = 6
d = 2*pi/D

heax = r*cos(d)
heay = r*sin(d)

hebx = r*cos(2*d)
heby = r*sin(2*d)

hecx = r*cos(3*d)
hecy = r*sin(3*d)

hedx = r*cos(4*d)
hedy = r*sin(4*d)

heex = r*cos(5*d)
heey = r*sin(5*d)

hefx = r*cos(6*d)
hefy = r*sin(6*d)

x = np.array([heax,hebx,hecx,hedx,heex,hefx,heax])
y = np.array([heay,heby,hecy,hedy,heey,hefy,heay])

print("""Las coordenadas para el hexagono inscrito
en una circunferencia de radio 2 son:
A = (%5.2f, %5.2f)
B = (%5.2f, %5.2f)
C = (%5.2f, %5.2f)
D = (%5.2f, %5.2f)
E = (%5.2f, %5.2f)
F = (%5.2f, %5.2f)"""%(heax, heay, hebx, heby, hecx, hecy, hedx, hedy, heex, heey, hefx, hefy))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='m')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Heptagono

V = 7
v = 2*pi/V

hepax = r*cos(v)
hepay = r*sin(v)

hepbx = r*cos(2*v)
hepby = r*sin(2*v)

hepcx = r*cos(3*v)
hepcy = r*sin(3*v)

hepdx = r*cos(4*v)
hepdy = r*sin(4*v)

hepex = r*cos(5*v)
hepey = r*sin(5*v)

hepfx = r*cos(6*v)
hepfy = r*sin(6*v)

hepgx = r*cos(7*v)
hepgy = r*sin(7*v)

x = np.array([hepax,hepbx,hepcx,hepdx,hepex,hepfx,hepgx,hepax])
y = np.array([hepay,hepby,hepcy,hepdy,hepey,hepfy,hepgy,hepay])

print("""Las coordenadas para el heptagono inscrito
en una circunferencia de radio 2 son:
A = (%5.2f, %5.2f)
B = (%5.2f, %5.2f)
C = (%5.2f, %5.2f)
D = (%5.2f, %5.2f)
E = (%5.2f, %5.2f)
F = (%5.2f, %5.2f)
G = (%5.2f, %5.2f)"""%(hepax, hepay, hepbx, hepby, hepcx, hepcy, hepdx, hepdy, hepex, hepey, hepfx, hepfy, hepgx, hepgy))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='b')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Octagono

C = 8
c = 2*pi/C

ocax = r*cos(c)
ocay = r*sin(c)

ocbx = r*cos(2*c)
ocby = r*sin(2*c)

occx = r*cos(3*c)
occy = r*sin(3*c)

ocdx = r*cos(4*c)
ocdy = r*sin(4*c)

ocex = r*cos(5*c)
ocey = r*sin(5*c)

ocfx = r*cos(6*c)
ocfy = r*sin(6*c)

ocgx = r*cos(7*c)
ocgy = r*sin(7*c)

ochx = r*cos(8*c)
ochy = r*sin(8*c)

x = np.array([ocax,ocbx,occx,ocdx,ocex,ocfx,ocgx,ochx,ocax])
y = np.array([ocay,ocby,occy,ocdy,ocey,ocfy,ocgy,ochy,ocay])

print("""Las coordenadas para el octagono inscrito
en una circunferencia de radio 2 son:
A = (%5.2f, %5.2f)
B = (%5.2f, %5.2f)
C = (%5.2f, %5.2f)
D = (%5.2f, %5.2f)
E = (%5.2f, %5.2f)
F = (%5.2f, %5.2f)
G = (%5.2f, %5.2f)
H = (%5.2f, %5.2f)"""%(ocax, ocay, ocbx, ocby, occx, occy, ocdx, ocdy, ocex, ocey, ocfx, ocfy, ocgx, ocgy, ochx, ochy))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='g')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Nonagono

Y = 9
y = 2*pi/Y

noax = r*cos(y)
noay = r*sin(y)

nobx = r*cos(2*y)
noby = r*sin(2*y)

nocx = r*cos(3*y)
nocy = r*sin(3*y)

nodx = r*cos(4*y)
nody = r*sin(4*y)

noex = r*cos(5*y)
noey = r*sin(5*y)

nofx = r*cos(6*y)
nofy = r*sin(6*y)

nogx = r*cos(7*y)
nogy = r*sin(7*y)

nohx = r*cos(8*y)
nohy = r*sin(8*y)

noix = r*cos(9*y)
noiy = r*sin(9*y)

x = np.array([noax,nobx,nocx,nodx,noex,nofx,nogx,nohx,noix,noax])
y = np.array([noay,noby,nocy,nody,noey,nofy,nogy,nohy,noiy,noay])


print("""Las coordenadas para el nonagono inscrito
en una circunferencia de radio 2 son:
A = (%5.2f, %5.2f)
B = (%5.2f, %5.2f)
C = (%5.2f, %5.2f)
D = (%5.2f, %5.2f)
E = (%5.2f, %5.2f)
F = (%5.2f, %5.2f)
G = (%5.2f, %5.2f)
H = (%5.2f, %5.2f)
I = (%5.2f, %5.2f) """%(noax, noay, nobx, noby, nocx, nocy, nodx, nody, noex, noey, nofx, nofy, nogx, nogy, nohx, nohy, noix, noiy))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='orange')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Decagono

X = 10
x = 2*pi/X

decax = r*cos(x)
decay = r*sin(x)

decbx = r*cos(2*x)
decby = r*sin(2*x)

deccx = r*cos(3*x)
deccy = r*sin(3*x)

decdx = r*cos(4*x)
decdy = r*sin(4*x)

decex = r*cos(5*x)
decey = r*sin(5*x)

decfx = r*cos(6*x)
decfy = r*sin(6*x)

decgx = r*cos(7*x)
decgy = r*sin(7*x)

dechx = r*cos(8*x)
dechy = r*sin(8*x)

decix = r*cos(9*x)
deciy = r*sin(9*x)

decjx = r*cos(10*x)
decjy = r*sin(10*x)

x = np.array([decax,decbx,deccx,decdx,decex,decfx,decgx,dechx,decix,decjx,decax])
y = np.array([decay,decby,deccy,decdy,decey,decfy,decgy,dechy,deciy,decjy,decay])


print("""Las coordenadas para el decagono inscrito
en una circunferencia de radio 2 son:
A = (%5.2f, %5.2f)
B = (%5.2f, %5.2f)
C = (%5.2f, %5.2f)
D = (%5.2f, %5.2f)
E = (%5.2f, %5.2f)
F = (%5.2f, %5.2f)
G = (%5.2f, %5.2f)
H = (%5.2f, %5.2f)
I = (%5.2f, %5.2f)
J = (%5.2f, %5.2f)"""%(decax, decay, decbx, decby, deccx, deccy, decdx, decdy, decex, decey, decfx, decfy, decgx, decgy, dechx, dechy, decix, deciy, decjx, decjy))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='plum')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Nonecagono

Z = 11
z = 2*pi/Z

undax = r*cos(z)
unday = r*sin(z)

undbx = r*cos(2*z)
undby = r*sin(2*z)

undcx = r*cos(3*z)
undcy = r*sin(3*z)

unddx = r*cos(4*z)
unddy = r*sin(4*z)

undex = r*cos(5*z)
undey = r*sin(5*z)

undfx = r*cos(6*z)
undfy = r*sin(6*z)

undgx = r*cos(7*z)
undgy = r*sin(7*z)

undhx = r*cos(8*z)
undhy = r*sin(8*z)

undix = r*cos(9*z)
undiy = r*sin(9*z)

undjx = r*cos(10*z)
undjy = r*sin(10*z)

undkx = r*cos(11*z)
undky = r*sin(11*z)

x = np.array([undax,undbx,undcx,unddx,undex,undfx,undgx,undhx,undix,undjx,undkx,undax])
y = np.array([unday,undby,undcy,unddy,undey,undfy,undgy,undhy,undiy,undjy,undky,unday])


print("""Las coordenadas para el undecagono inscrito
en una circunferencia de radio 2 son:
A = (%5.2f, %5.2f)
B = (%5.2f, %5.2f)
C = (%5.2f, %5.2f)
D = (%5.2f, %5.2f)
E = (%5.2f, %5.2f)
F = (%5.2f, %5.2f)
G = (%5.2f, %5.2f)
H = (%5.2f, %5.2f)
I = (%5.2f, %5.2f)
J = (%5.2f, %5.2f)
K = (%5.2f, %5.2f)"""%(undax, unday, undbx, undby, undcx, undcy, unddx, unddy, undex, undey, undfx, undfy, undgx, undgy, undhx, undhy, undix, undiy, undjx, undjy, undkx, undky))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='gold')
ax.add_patch(circulo)

plt.legend()
plt.show()

# Dodecagono

Ñ = 12
ñ = 2*pi/Ñ

dodax = r*cos(ñ)
doday = r*sin(ñ)

dodbx = r*cos(2*ñ)
dodby = r*sin(2*ñ)

dodcx = r*cos(3*ñ)
dodcy = r*sin(3*ñ)

doddx = r*cos(4*ñ)
doddy = r*sin(4*ñ)

dodex = r*cos(5*ñ)
dodey = r*sin(5*ñ)

dodfx = r*cos(6*ñ)
dodfy = r*sin(6*ñ)

dodgx = r*cos(7*ñ)
dodgy = r*sin(7*ñ)

dodhx = r*cos(8*ñ)
dodhy = r*sin(8*ñ)

dodix = r*cos(9*ñ)
dodiy = r*sin(9*ñ)

dodjx = r*cos(10*ñ)
dodjy = r*sin(10*ñ)

dodkx = r*cos(11*ñ)
dodky = r*sin(11*ñ)

dodlx = r*cos(12*ñ)
dodly = r*sin(12*ñ)

x = np.array([dodax,dodbx,dodcx,doddx,dodex,dodfx,dodgx,dodhx,dodix,dodjx,dodkx,dodlx,dodax])
y = np.array([doday,dodby,dodcy,doddy,dodey,dodfy,dodgy,dodhy,dodiy,dodjy,dodky,dodly,doday])


print("""Las coordenadas para el dodecagono inscrito
en una circunferencia de radio 2 son:
A = (%5.2f, %5.2f)
B = (%5.2f, %5.2f)
C = (%5.2f, %5.2f)
D = (%5.2f, %5.2f)
E = (%5.2f, %5.2f)
F = (%5.2f, %5.2f)
G = (%5.2f, %5.2f)
H = (%5.2f, %5.2f)
I = (%5.2f, %5.2f)
J = (%5.2f, %5.2f)
K = (%5.2f, %5.2f)
L = (%5.2f, %5.2f)"""%(dodax, doday, dodbx, dodby, dodcx, dodcy, doddx, doddy, dodex, dodey, dodfx, dodfy, dodgx, dodgy, dodhx, dodhy, dodix, dodiy, dodjx, dodjy, dodkx, dodky, dodlx, dodly))

circulo = plt.Circle((0,0), radius=r, color='gainsboro')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='greenyellow')
ax.add_patch(circulo)

plt.legend()
plt.show() 
 
