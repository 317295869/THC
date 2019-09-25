#
# Eduardo Alexis Valencia Dorantes
# python 3.5.3
# 24/09/2019 25/09/2019
#
#
from math import sin, cos, sqrt ,pi

import matplotlib.pyplot as plt
import numpy as np

#plt.show()


l = 5
a = 2*pi/l


x1 = cos(a)
x2 = cos(2*a)
x3 = cos(3*a)
x4 = cos(4*a)
x5 = cos(5*a)

y1 = sin(a)
y2 = sin(2*a)
y3 = sin(3*a)
y4 = sin(4*a)
y5 = sin(5*a)

x = np.array([x1,x2,x3,x4,x5,x1])
y = np.array([y1,y2,y3,y4,y5,y1])


print("""Las coordenadas del pentagono
son:
A = (%5.2f,%5.2f)
B = (%5.2f,%5.2f)
C = (%5.2f,%5.2f)
D = (%5.2f,%5.2f)
E = (%5.2f,%5.2f)
"""%(x1, y2, x2, y2, x3, y3 ,x4 ,y4 ,x5 ,y5))

plt.legend()
plt.show()

