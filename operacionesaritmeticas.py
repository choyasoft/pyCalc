def Sumar(sumando1,sumando2):
	return sumando1+sumando2

def Restar(minuendo,sustraendo):
	return minuendo-sustraendo

def Multiplicar(multiplicando,multiplicador):
	return multiplicando*multiplicador

def Dividir(dividendo,divisor):
	try:
		resultado = dividendo/divisor
		return resultado
	except ZeroDivisionError:
		return -1