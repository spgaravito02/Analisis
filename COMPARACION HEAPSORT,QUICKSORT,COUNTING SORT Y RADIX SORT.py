print "Solangie Paola Garavito 624702"
print ""
print "****************************************************"
print "*******COMPARACION HEAPSORT,QUICKSORT,**************"
print "*******  CCOUNTING SORT Y RADIX SORT  *************"
print "****************************************************"

import random
import time

# Funcion para crear numeros aleatorios
def  numeros(x):
    vec_ini=[]
    vec_ini2=[]
    vec_ini3=[]
    for i in range(0,x):
        dato=(random.choice (range(19))*random.choice(range(58)))/3
        vec_ini.append( [] )
        vec_ini[-1].append( dato )
        vec_ini2.append( [] )
        vec_ini2[-1].append( dato )
        vec_ini3.append( [] )
        vec_ini3[-1].append( dato )
    return vec_ini,vec_ini2,vec_ini3

# Funcion para ordenar ascendentemente por el metodo HEAPSORT
def ordenar_heapsort():
    for i in range(1,x):
        for j in range (0,x-1):
            comp=comp+1
            if vector[j]>vector[j+1]:
                aux=vector[j]
                vector[j]=vector[j+1]
                vector[j+1]=aux
                inter = inter+1       
    print "Comparaciones:",comp
    print "Intercambios:",inter
    return vector
                     


        

#Arranque del programa
cant=input("Ingrese la cantidad de numeros que desea ordenar: ")
vec_burbuja,vec_merg,vec_insert = numeros(cant)
print ""
print "El vector a ordenar es:",vec_insert
#Imprime Metodo Burbuja
print ""
print "-----------------------METODO BURBUJA-----------------------"
ini_relog= time.clock ()
vec_ord=ordenar_burbuja(vec_burbuja,cant)
fin_relog=time.clock ()-ini_relog
print "Tiempo proceso:",fin_relog
print ""
#Imprime Metodo Insercion
print ""
print "-----------------------METODO INSERCION-----------------------"
ini_relog= time.clock ()
vec_ord=ordenar_insert(vec_insert,cant)
fin_relog=time.clock ()-ini_relog
print "Tiempo proceso:",fin_relog
print ""
#Imprime Metodo Mersort
print "-----------------------METODO MERGSORT------------------------"
ini_relog= time.clock ()
vec_ord=divide_mergsort(vec_merg)
fin_relog=time.clock ()-ini_relog
print "Tiempo proceso:",fin_relog
print ""
print "El vector ordenado ascendentemente es:",vec_ord

raw_input()

