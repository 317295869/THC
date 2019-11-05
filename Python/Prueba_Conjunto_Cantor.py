#Fractal del conjunto de Cantor

import matplotlib.pyplot as plt
import numpy as np

plt.axis([0,30,0,20])

l=30
n=15

x1=0
y1=n

x2=l
y2=n

x = np.array([x1,x2])
y = np.array([y1,y2])
plt.plot(x, y, color='b')


while n>=5:
    x1=0
    y1=n-3

    x2= l/3
    y2= n-3

    x3= (l/3)*2
    y3= n-3

    x4= l
    y4= n-3

    xiz = np.array([x1,x2])
    yiz = np.array([y1,y2])

    plt.plot(xiz,yiz, color='b')       

    xder = np.array([x3,x4])
    yder = np.array([y3,y4])

    plt.plot(xder,yder, color='b')

    l=l/3
    n=n-3

    
# plt.legend()
plt.show()  

"""for i in list(range(2**n)):
        for a coordenadas
        
        x = np.array([x1,x2])
        y = np.array([y1,y2])
        plt.plot(xiz,yiz, color='b')

    n=n+1"""

