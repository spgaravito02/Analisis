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
    for i in range(0,x):
        dato=(random.choice (range(19))*random.choice(range(58)))/3
        vec_ini.append( [] )
        vec_ini[-1].append( dato )
    return vec_ini

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

def ordena_merg (arreglo1,n1,arreglo2,n2,arreglo3):
    x1=0
    x2=0
    x3=0
    while x1<n1 and x2<n2:
        if arreglo1[x1]<arreglo2[x2]:
            arreglo3[x3] = arreglo1[x1]
            x1=x1+1
        else:
            arreglo3[x3] = arreglo2[x2];
            x2=x2+1
            
    while x1<n1:
        arreglo3[x3] = arreglo1[x1]
        x1=x1+1;
        x3=x3+1;
        
    while x2<n2:
        arreglo3[x3] = arreglo2[x2]
        x2=x2;
        x3=x3;
    return arreglo3

def ordenar_asc_merg(vector,x):
    comp=0
    inter=0
    vec1=[]
    vec2=[]
    ini_relog= time.clock ()
    if x>1:
        if (x / 2)== 0:
            n1=n2=(x/2)
        else:
            n1=x/2
            n2=n1+1
        for i in range(0,n1):
            vec1[i]=vector[i]
            i=i+1
        for j in range(0,n2):
            vec2[j]=vector[i];
            i=i+1
            j=j+1
        ordenar_asc_merg(n1,vec1)
        ordenar_asc_merg(n2,vec2)
        ordena_merg(vec1, n1, vec2, n2, vec)
    fin_relog=time.clock ()-ini_relog
    print "Tiempo proceso:",fin_relog
    return vector

        

#Arranque del programa
cant=input("Ingrese la cantidad de numeros que desea ordenar: ")
vec_des=numeros(cant)
print ""
print "El vector a ordenar es:",vec_des

#Imprime Metodo Insercion
print ""
print "-----------------------METODO INSERCION-----------------------"
vec_ord=ordenar_insert(vec_des,cant)
print ""

print "El vector ordenado ascendentemente es:",vec_ord
print ""
print "-----------------------METODO MERGSORT-----------------------"
vec_ord=ordenar_asc_merg(vec_des,cant)
print ""

print "El vector ordenado ascendentemente es:",vec_ord
raw_input()

