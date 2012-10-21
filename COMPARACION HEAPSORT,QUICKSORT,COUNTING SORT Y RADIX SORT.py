print "Solangie Paola Garavito 624702"
print ""
print "****************************************************"
print "*******COMPARACION HEAPSORT,QUICKSORT,**************"
print "*******  COUNTING SORT Y RADIX SORT  *************"
print "****************************************************"

import random
import time

# Funcion para crear numeros aleatorios
def  numeros(x):
    vec_ini=[]
    vec_ini2=[]
    vec_ini3=[]
    vec_ini4=[]
    for i in range(0,x):
        dato=(random.choice (range(15))*random.choice(range(58)))/3
        vec_ini.append(dato)
        vec_ini2.append(dato)
        vec_ini3.append(dato)
        vec_ini4.append(dato)
    return vec_ini,vec_ini2,vec_ini3,vec_ini4

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
def ordenar_quicksort(vector,izq,der):
    i=izq
    j=der
    x=vector[(izq+der)/2]

    while (i<=j):
        while vector [i] < x and j<=der:
            i=i+1
        while x< vector [j] and j>izq:
            j=j-1
        if i<=j:
            aux = vector [i]
            vector [i]=vector [j]
            vector [j]=aux
            i=i+1
            j=j-1
        if izq < j:
            ordenar_quicksort (vector,izq,j)
    if i<der:
        ordenar_quicksort (vector,i,der)
    return vector

# Funcion para ordenar ascendentemente por el metodo COUNTING SORT
def ordenar_counting(vector):
    maximo= max(vector)
    minimo= min(0, min(vector))
    count_vector= [0]*(maximo-minimo+1)

    for j in vector:
        count_vector[j]+=count_vector[j]+1

    vector_ordenado=[]
    for i in range (minimo, maximo+1):
        if count_vector[i]>0:
            for k in range(0,count_vector[i]):
                vector_ordenado.append(i)
    return vector_ordenado
    

 
#Arranque del programa
cant=input("Ingrese la cantidad de numeros que desea ordenar: ")
vec_heapsort,vec_quicksort,vec_counting,vec_insert = numeros(cant)
print ""
print "El vector a ordenar es:",vec_insert
#Imprime Metodo Heapsort
print ""
print "-----------------------METODO HEAPSORT-----------------------"
print ""
ini_relog= time.clock ()
vec_ord=ordenar_heapsort(vec_heapsort,cant)
fin_relog=time.clock ()-ini_relog
print "Vector Ordenado:",vec_ord
print "Tiempo proceso:",fin_relog
print ""
print "-----------------------METODO QUICKSORT-----------------------"
print ""
ini_relog= time.clock ()
vec_ord=ordenar_quicksort(vec_quicksort,0,cant-1)
fin_relog=time.clock ()-ini_relog
print "Vector Ordenado:",vec_ord
print "Tiempo proceso:",fin_relog
print ""
print "-----------------------METODO COUNTING SORT-----------------------"
print ""
ini_relog= time.clock ()
vec_ord=ordenar_counting(vec_counting)
fin_relog=time.clock ()-ini_relog
print "Vector Ordenado:",vec_ord
print "Tiempo proceso:",fin_relog
print ""


raw_input()

