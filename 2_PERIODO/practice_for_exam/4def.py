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

def calculate_grade(number):
    if number > 0.9:
        print('A')
    elif number > 0.8:
        print('B')
    elif number > 0.7:
        print('C')
    elif number > 0.6:
        print('D')
    elif number <= 0.6:
        print('F')

number = float(input('Introduce a number between 0-1: '))
if number <= 1 and number >= 0:
    calculate_grade(number=number)
else:
    print('Incorrect Score')