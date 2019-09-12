#
# Eduardo Alexis Valencia Dorantes
# python 3.5.3
# 10/09/2019
# 12/09/2019
#
# Calcula la posicion de una pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos

v0 = 5
g = 9.8
t = 0.6
y = v0*t -0.5*g*t**2

print(y)
print('En el tiempo t=%g segundos, la altura de la pelota es %.2f metros'%(t,y))
print("""
En t=%g segundos, la pelota con
velocidad inicial v0=%.3E m/s
se encuentra a %.2f metros de altura.""" % (t,v0, y) )





