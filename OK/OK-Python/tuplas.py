tupla = ('M', 27, 'L', 'E', 'I', 'O', 'U')

for i in range(len(tupla)):
    x=tupla.count(tupla[i])
    print("El elemento %s, se repite: %d veces"%(str(tupla[i]),x))
