print "Solangie Paola Garavito 624702"
print ""
print "****************************************************"
print "************* CALCULO SERIE FIBONACCI **************"
print "****************************************************"
valor = input("Ingrese el valor maximo que desea generear en la serie: ")
num1=0
num2=1
if valor>0:
    print "Los valores de la serie son:"
    print num1
    print num2
    for i in range(0,valor):
        num3=num1+num2
        num1=num2
        num2=num3
        print num3
else:
    print "El valor ingresado no es valido.Ingrese un valor mayor a 0"

raw_input()


