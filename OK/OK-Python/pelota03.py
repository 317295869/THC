# !/usr/bin/python3
# Eduardo Alexis Valencia Dorantes
# python 3.5.3
# 12/09/2019
#
# Calcula la posición de una pelota con una velocidad inicial
# de 5 m/s y un tiempo de 0.6 segundos utilizando nombres de variables
# descriptivos pero muuuuuy largos

velocidad_inicial = 5
constante_de_gravedad = 9.81
TIEMPO = 0.6
PosicionVerticalDeLaBola = velocidad_inicial*TIEMPO -\
                           0.5*constante_de_gravedad*TIEMPO**2
print(PosicionVerticalDelaBola)
