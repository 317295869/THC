#Valencia Dorantes Eduardo Alexis 
#29/10/19
#
#Evaluación práctica
"""A partir de un rectangulo de base x y altura 1 definiremos la raíz cuadrada\
de un número cualquiera que sea mayor a cero"""

print('x = 81')

bases=[]
alturas=[]
b=81
x=b
h=1
print(" rectangulo   b       h")
print("     0      %.2f   %.2f"%(b,h))
for i in range(1,7):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("     %g      %5.2f  %5.2f"%(i, b, h))
print('..........................')

print('x = 95')

bases=[]
alturas=[]
b=95
x=b
h=1
print(" rectangulo   b       h")
print("     0      %.2f   %.2f"%(b,h))
for i in range(1,7):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("     %g      %5.2f  %5.2f"%(i, b, h))
print('..........................')

print('x = .5')

bases=[]
alturas=[]
b=.5
x=b
h=1
print(" rectangulo   b       h")
print("     0       %.2f   %.2f"%(b,h))
for i in range(1,7):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("     %g      %5.2f  %5.2f"%(i, b, h))
print('..........................')

print('x = .125')

bases=[]
alturas=[]
b=.125
x=b
h=1
print(" rectangulo   b       h")
print("     0       %.2f   %.2f"%(b,h))
for i in range(1,7):
    b=(b+h)/2
    h=x/b
    bases.append(b)
    alturas.append(h)
    print("     %g      %5.2f  %5.2f"%(i, b, h))
    
