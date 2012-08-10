print "Solangie Paola Garavito 624702"
print ""
print "****************************************************"
print "*******ORDENAMIENTO POR INSERCION Y MERGSORT********"
print "****************************************************"

import random
import time

# Funcion para crear numeros aleatorios
def  numeros(x):
    vec_ini=[]
    vec_ini2=[]
    for i in range(0,x):
        dato=(random.choice (range(19))*random.choice(range(58)))/3
        vec_ini.append( [] )
        vec_ini[-1].append( dato )
        vec_ini2.append( [] )
        vec_ini2[-1].append( dato )
    return vec_ini,vec_ini2

# Funcion para ordenar ascendentemente por el metodo de la Insercion
def ordenar_insert(vector,x):
    comp=0
    inter=0
    ini_relog= time.clock ()
    for i in range(0,x):
        comp=comp+1
        aux=vector[i]
        j=i
        while j>0 and aux<vector[j-1]:
            vector[j]=vector[j-1]
            j=j-1
            inter = inter+1
        vector[j]=aux;
    fin_relog=time.clock ()-ini_relog
    print "Comparaciones:",comp
    print "Intercambios:",inter
    print "Tiempo proceso:",fin_relog
    return vector


# Funcion para ordenar ascendentemente por el metodo de Mergsort
def ordena_mergsort (arreglo1,n1,arreglo2,n2):
    vect_ord=[]
    i=0
    j=0
    while i < n1 and j < n2:
        if  arreglo1[i]<=arreglo2[j]:
            vect_ord.append(arreglo1[i])
            i+=1
        else:
            vect_ord.append(arreglo2[j])
            j+=1
    vect_ord +=arreglo1[i:]
    vect_ord +=arreglo2[j:]
    
def divide_mergsort(vector,x):
    n1=0
    n2=0
    if x>1:
        print vector
        if (x%2==0):
            n1=n2= x / 2                     
        else:
            n1=x / 2
            n2=n1+1
        mitad=len(vector)/2
        print vector[:mitad]
        print vector[mitad:]
        arreglo1=divide_mergsort(vector[:mitad],n1)
        print arreglo1
        arreglo2=divide_mergsort(vector[mitad:],n2)
        print arreglo2
        return ordena_mergsort(arreglo1,n1,arreglo2,n2)                          


        

#Arranque del programa
cant=input("Ingrese la cantidad de numeros que desea ordenar: ")
vec_merg,vec_insert = numeros(cant)
print ""
print "El vector a ordenar es:",vec_insert
#Imprime Metodo Insercion
print ""
print "-----------------------METODO INSERCION-----------------------"
vec_ord=ordenar_insert(vec_insert,cant)
print ""
#Imprime Metodo Mersort
print "-----------------------METODO MERGSORT------------------------"
vec_ord=divide_mergsort(vec_merg,cant)
print ""
#print "Tiempo proceso:",fin_relog
print ""
print "El vector ordenado ascendentemente es:",vec_ord

raw_input()

