# !/usr/bin/python3.6
#
# Eduardo Alexis Valencia Dorantes
# Python 3.6.8
# 
#

cantidad_bugs=input()

#import sys
#nivel_bugs = str(sys.stdin.readline())
nivel_bugs=str(input())
nivel_bugs=nivel_bugs.split()

mi_nivel=1
vida=10
vida_bandera=vida
contSubirNivel=0
perdedor=0
contBugs=0

for bug in nivel_bugs:
        bug=int(bug)
        #print("El bug es %d"%(bug))
        if bug>mi_nivel:
            vida=vida-(bug*2)
        if bug<mi_nivel:
            vida=vida-1
        if bug==mi_nivel:
            vida=vida-bug
        #print("Tu vida es %d"%(vida))
            
        
        if vida<=0:
            print("You have died. Reached level %d and killed %d bugs"%(mi_nivel,contBugs))
            perdedor=1
            break
        
        contSubirNivel+=1
        contBugs+=1
        #print("contador subir nivel %d"%(contSubirNivel))
        
        if contSubirNivel==3:
            contSubirNivel=0
            mi_nivel+=1
            vida_bandera=vida_bandera+5
            vida=vida_bandera

        #print("Mi nivel es %d"%(mi_nivel))

if perdedor == 0:        
    print("You have won! Reached level %d and killed %d bugs"%(mi_nivel,contBugs))
