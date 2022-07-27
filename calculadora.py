import operacionesaritmeticas

def Sumar():
	sumando1 = int(input("Introduce primer sumando: "))
	sumando2= int(intpu("Introduce segundo sumando: "))
	print("Resultado: ", operacionesaritmeticas.Sumar(sumando1,sumando2))

def Restar():
	minuendo = int(input("Introduce el minuendo: "))
	sustraendo=int(input("Introduce el sustraendo: "))
	print("Resultado: ", operacionesaritmeticas.Restar(minuendo,sustraendo))

def Multiplicar():
	multiplicando = int(input("Introduce el multiplicando: "))
	multiplicador = int(input("Introduce el multiplicador: "))
	print("Resultado: ", operacionesaritmeticas.Multiplicar(multiplicando, multiplicador))

def Dividir():
	dividendo = int(input("Introduce el dividendo: "))
	divisor = int(input("Introduce el divisor: "))
	print("Resultado: ", operacionesaritmeticas.Dividir(dividendo,divisor))


def Calculadora():
	fin = False
	while not(fin):
		opc = int(input("Opción: "))
		if(opc==1):
			Sumar()
		elif(opc==2):
			Restar()
		elif(opc==3):
			Multiplicar()
		elif(opc==4):
			Dividir()
		elif(opc==5):
			fin = 1
print("""*#*#*  C A L C U L A D O R A    P Y T H O N   *#*#*
1) Suma
2) Resta
3) Multiplicar 
4) Dividir
5) Salir""")
Calculadora()

