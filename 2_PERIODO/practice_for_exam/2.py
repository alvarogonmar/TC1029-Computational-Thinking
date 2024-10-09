#2
#Escribe un programa que convierta pies, pulgadas y yardas a centímetros, para lo cual debes definir 3 funciones:

#Función que reciba una cantidad de pies (entero positivo) y devuelva el equivalente a centímetros.
#Función que reciba una cantidad de pulgadas (entero positivo) y devuelva el equivalente a centímetros.
#Función que reciba una cantidad de yardas (entero positivo) y devuelva el equivalente en centímetros.
#Entrada:
#La opción a ejecutar (1 – pies a cm, 2 - pulgadas a cm, 3 – yardas a cm).
#Un valor entero positivo que corresponde a la cantidad en la medida de acuerdo con la opción tecleada (sólo el número).

#Salida:
#La cantidad equivalente en centímetros.
#En caso de que el número de opción sea diferente a 1, 2, o 3 se desplegará el mensaje: Error.
#En caso de que el valor a convertir sea 0 o menor se desplegará el mensaje: Error


def feet(a):
    result = a * 30.48
    print(result)

def inches(b):
    result = b * 2.54
    print(result)

def yards(c):
    result = c * 91.44
    print(result)

option = int(input('Choose: 1-Feets. 2-Inches. 3-Yards. To cm: '))
if option == 0:
    print('ERROR')
else:
    value = float(input('Measure: '))
    if value != 0:
        if option == 1:
            feet(value)
        elif option == 2:
            inches(value)
        elif option == 3:
            yards(value)
    else:
        print('ERROR')