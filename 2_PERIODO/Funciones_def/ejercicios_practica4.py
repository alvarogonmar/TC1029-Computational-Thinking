# Escribe un programa en el cual definas la función llamada calcula_grado. Esta función debe recibir un número flotante entre 0 y 1, 
# y debe regresar una nota alfabética de acuerdo con la siguiente tabla.

# Score	Nota
# >0.9	A
# >0.8	B
# >0.7	C
# >0.6	D
# <=0.6	F
 
# Entrada
# Un número flotante entre 0 y 1.
# Salida
# La letra correspondiente al score asignado de acuerdo con la tabla de arriba.
# Si la entrada no está dentro del rango de 0 a 1 (inclusive), la función debe regresar la leyenda "score incorrecto".

valor = float(input('Introduzca el valor del score (un valor entre 0 y 1): '))

def calcula_grado(valor):
    if valor < 0 or valor > 1:
        print('Score incorrecto')
    else:
        if valor > 0.9:
            return 'A'
        elif valor > 0.8:
            return 'B'
        elif valor > 0.7:
            return 'C'
        elif valor > 0.6:
            return 'D'
        else:
            return 'F'
        
grado = calcula_grado(valor)
print(valor)
print(f'La nota obetnida es: {grado}')