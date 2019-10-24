def Regla30 (x,y,z):
    if (x,y,z) == (1,1,1):
        resultado = 0
    if (x,y,z) == (1,1,0):
        resultado = 0
    if (x,y,z) == (1,0,1):
        resultado = 0
    if (x,y,z) == (1,0,0):
        resultado = 1
    if (x,y,z) == (0,1,1):
        resultado = 1
    if (x,y,z) == (0,1,0):
        resultado = 1
    if (x,y,z) == (0,0,1):
        resultado = 1
    if (x,y,z) == (0,0,0):
        resultado = 0
    return(resultado)

n = 43
c = [0]*n
c[n//2] = 1


e=[]
for i in range(n):
    if c[i] == 1:
        e.append(i)
print(e)
Y=[21]*len(e)


E = []
t = 0
for valor in c:
    if valor == 1:
        E.append(t)
    t += 1    

c = e.copy()
print(c)
for i in range(22):
    e=[]
    for i in range(43):
        e.append(Regla30(c[i-1],c[i],c[(i+1)%43]))
    c = e.copy()
    print(c)
        
print(E)
