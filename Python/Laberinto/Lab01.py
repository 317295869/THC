def cargarlaberinto(laberinto):
    archivo=open("LEduardo.txt","r")
    l1=" "
    l=[]
    while l1:
        l1=archivo.readline()
        if l1:
            l1=l1.rstrip()
            l1=[int(x) for x in list(l1)]
            l.append(l1)
    return(l)
l=cargarlaberinto("LEduardo.txt")
print(l)
