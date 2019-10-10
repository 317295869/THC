#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 09-10-2019
#
acumulado = 0
numero_veces = [7, 8, 16, 9, 13, 6, 4]
for i in range(len(numero_veces)):
	if numero_veces[i]>= 10:
		print(numero_veces[i]*3+18.5)
	else:
		print(numero_veces[i]*2/7 + 2.1)

print(acumulado)

numero_veces1 = [41, 65, 89, 74, 85, 32, 14, 54, 85, 4, 6, 6, 4, 7, 8, 5, 4, 1,\
                2, 4, 4, 77, 85, 96, 12, 45]

def totalPolen(numero_veces):
    acumulado = 0
    for j in range(len(numero_veces)):
            if numero_veces[j]>= 10:
                    acumulado = acumulado + numero_veces[j]*3 + 18.5
                    print(numero_veces[j]*3 + 18.5)
            else:
                    acumulado = acumulado + numero_veces[j]*3 + 18.5
                    print(numero_veces[j]*3 + 18.5)
    return(acumulado)



    
