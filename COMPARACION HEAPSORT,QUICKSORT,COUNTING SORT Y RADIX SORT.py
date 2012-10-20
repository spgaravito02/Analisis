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
def ordenar_heapsort(vector,tam):
    inicio = (tam-2)/2
    while inicio >= 0:
        crearheap(vector, inicio, tam-1)
        inicio=inicio-1
    fin = tam-1    
    while fin > 0:
        vector[fin], vector[0] = vector[0], vector[fin]
        crearheap(vector, 0, fin-1)
        fin = fin-1
    return vector

def crearheap(vector, inicio, fin):
    i = inicio
    while i * 2 + 1 <= fin:
        j = i * 2 + 1
        if j + 1 <= fin and vector[j] < vector[j + 1]:
            j=j+1
        if j <= fin and vector[i] < vector[j]:
            vector[i], vector[j] = vector[j], vector[i]
            i = j
        else:
            return

# Funcion para ordenar ascendentemente por el metodo QUICKSORT
def vec_quicksort(vector,tam):
    inicio = (tam-2)/2
    while inicio >= 0:
        crearheap(vector, inicio, tam-1)
        inicio=inicio-1
    fin = tam-1    
    while fin > 0:
        vector[fin], vector[0] = vector[0], vector[fin]
        crearheap(vector, 0, fin-1)
        fin = fin-1
    return vector


    



        

#Arranque del programa
cant=input("Ingrese la cantidad de numeros que desea ordenar: ")
vec_heapsort,vec_quicksort,vec_insert = numeros(cant)
print ""
print "El vector a ordenar es:",vec_insert
#Imprime Metodo Heapsort
print ""
print "-----------------------METODO HEAPSORT-----------------------" 
ini_relog= time.clock ()
vec_ord=ordenar_heapsort(vec_heapsort,cant)
fin_relog=time.clock ()-ini_relog
print "Vector Ordenado:",vec_ord
print "Tiempo proceso:",fin_relog
print ""
print "-----------------------METODO QUICKSORT-----------------------" 
ini_relog= time.clock ()
vec_ord=ordenar_quicksort(vec_quicksort,cant)
fin_relog=time.clock ()-ini_relog
print "Vector Ordenado:",vec_ord
print "Tiempo proceso:",fin_relog
print ""


raw_input()

