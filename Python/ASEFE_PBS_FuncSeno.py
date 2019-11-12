#
#
#
#

def seno(alfa):
    alfa = 0.1
    Beta = alfa/2**5
    resultado = Beta
    return(resultado) 
    
if __name__ == "__main__":
    seno(.5)
    print("Este bloque se ejecuta si el programa \
es llamado desde IDLE, la variable __name__ tiene \
almacenada la cadena '__main__' ")
    print(__name__)
else:
    print("Si el archivo se utiliza como modulo,\
 es decir se importa, la variable __name__ contiene\
el nombre nombre del archivo")
    print(__name__)
