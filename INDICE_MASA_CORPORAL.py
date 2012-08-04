print "Solangie Paola Garavito 624702"
print ""
print "****************************************************"
print "******** CALCULO DE INDICE DE MASA CORPORAL ********"
print "****************************************************"


peso = raw_input ("Ingrese su peso: ")
peso=float(peso)
estatura = raw_input ("Ingrese su estatura: ")
estatura=float(estatura)

imc=peso/(estatura**2)
print "Su indice de masa corporal es : ",imc
print "Su clasificacion es:"
if imc<=16.00:
        print "Delgadez severa"
elif imc<16.99 and imc>16.01 :
        print "Delgadez moderada"
elif imc<18.49 and imc>17.00:
	print "Delgadez no muy pronunciada"
elif imc<24.99 and imc>18.50:
	print "Normal"
elif imc<29.99 and imc>25.00:
	print "Preobeso"
elif imc<34.99 and imc>30.00:
	print "Obeso tipo I"
elif imc<39.99 and imc>35.00:
	print "Obeso tipo I"
elif imc>=40.00:
	print "Obeso tipo III"

raw_input()



