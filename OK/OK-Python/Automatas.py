# !/usr/bin/python3.6
#
# Valencia Dorantes Eduardo Alexis
# 17/10/19
#
#
# Grafica la evolucion de automatas con base a la regla 30

import matplotlib.pyplot as plt
def regla30(a,i,s):
    """ Regresa el resultado en base a
 a la regla 30"""
    
    if a == 1 and i == 1 and s == 1:
        resultado = 0
        
    if a == 1 and i == 1 and s == 0:
        resultado = 0
        
    if a == 1 and i == 0 and s == 1:
        resultado = 0
        
    if a == 0 and i == 0 and s == 0:
        resultado = 0
        
    if a == 1 and i == 0 and s == 0:
        resultado = 1
        
    if a == 0 and i == 1 and s == 1:
        resultado = 1
        
    if a == 0 and i == 1 and s == 0:
        resultado = 1
        
    if a == 0 and i == 0 and s == 1:
        resultado = 1
        
    return(resultado)


n = 43
cel = [0]*43
cel[43//2] = 1
m=[i for i,x in enumerate(cel) if x== 1]
print(m)
plt.plot([m],[1],"sb")

for x in range(21):
    ne = []
    for i in range(43):
        ne.append(regla30(cel[i-1],cel[i],cel[(i+1)%43]))
    cel = ne.copy()
    m=[i for i,x in enumerate(cel) if x==1]
    print(m)
    plt.plot([m],[-x],"sb")

plt.show()
