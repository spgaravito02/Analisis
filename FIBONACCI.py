print "Solangie Paola Garavito 624702"
print "Sucesion de Fibonacci:es la sucesion infinita de numeros naturales"
print "esta inicia con 0 y 1, y a partir de ahi cada elemento es la suma"
print "de los dos anteriores."
print ""
print "****************************************************"
print "************* CALCULO SERIE FIBONACCI **************"
print "****************************************************"

valor = input("Ingrese el numero de la serie que desea generear: ")
num1=0
num2=1
if valor>0:
    print "Los valores de la serie son:"
    print num1
    print num2
    for i in range(0,valor-2):
        num3=num1+num2
        num1=num2
        num2=num3
        print num3
else:
    print "El valor ingresado no es valido.Ingrese un valor mayor a 0"

raw_input()


