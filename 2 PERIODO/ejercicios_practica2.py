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

opcion = int(input('Qué desea realizar: 1-pies a cm, 2 - pulgadas a cm, 3-yardas a cm: '))
valor = int(input('Ingrese el valor que quiere convertir: '))
def pies(a):
    resultado = a * 30.48
    print(resultado)

def pulgadas(b):
    resultado = b * 2.54
    print(resultado)

def yardas(c):
    resultado = c * 91.44
    print(resultado)

if opcion == 0:
    print('Error')
    if valor != 0:
        if opcion == 1:
            pies(valor)
        elif opcion == 2:
            pulgadas(valor)
        elif opcion == 3:
            yardas(valor)
        else:
            print('Opción no Válida')
    else:
        print('Opción no Válida')