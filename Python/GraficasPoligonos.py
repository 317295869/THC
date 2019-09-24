from math import sin, cos, sqrt, pi

import matplotlib.pyplot as plt
import numpy as np

r = 5
l = 5
a = 2*pi/l


x1 = r*cos(a)
x2 = r*cos(2*a)
x3 = r*cos(3*a)
x4 = r*cos(4*a)
x5 = r*cos(5*a)

y1 = r*sin(a)
y2 = r*sin(2*a)
y3 = r*sin(3*a)
y4 = r*sin(4*a)
y5 = r*sin(5*a)

x = np.array([x1,x2,x3,x4,x5,x1])
y = np.array([y1,y2,y3,y4,y5,y1])


print("""Las coordenadas del pentagono
inscrito en una circunferencia de radio %f
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
"""%(r, x1, y2, x2, y2, x3, y3 ,x4 ,y4 ,x5 ,y5))

circulo = plt.Circle((0,0), radius=r, color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='r')
ax.add_patch(circulo)



plt.legend()
plt.show() # comenten esta linea desde el inicio y descomenten la siguientem ¿hubo algun cambio?
#plt.draw() 

l = 3
a = 2*pi/l
R = pi

x1 = 5*cos(R + a)
x2 = 5*cos(R + 2*a)
x3 = 5*cos(R + 3*a)

y1 = 5*sin(R + a)
y2 = 5*sin(R + 2*a)
y3 = 5*sin(R + 3*a)

x = np.array([x1,x2,x3,x1])
y = np.array([y1,y2,y3,y1])

circulo= plt.Circle((0,0), radius= 5,color='b')
ax=plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.set_xlim([ -(r+1),(r+1) ])
ax.set_ylim([ -(r+1),(r+1) ])
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(x, y, label='linear', color='r')
ax.add_patch(circulo)

plt.legend()
plt.show()
