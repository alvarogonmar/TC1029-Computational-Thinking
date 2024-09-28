#LISTA AL REVES
#Escribe un programa que lea los valores enteros y los agregue a una lista, dejara de leer al leer el valor de -1.
#El programa debe crear otra lista que contenga los valores de la primera lista, pero en orden invertido. Luego debe mostrar ambas

#Entrada
#Una lista de valores enteros positivos, uno en cada renglon, finaliza la captura con -1

lista = []
num = []

num = int(input('Ingrese los numeros para ponerlos en orden invertido(-1 para finalizar de poner): '))
while num != -1:
    lista.append(num)
    num = int(input('Ingrese los numeros para ponerlos en orden invertido(-1 para finalizar de poner): '))

lista_invertida = lista[::-1]

print('Lista original:', lista)
print('Lista invertida:', lista_invertida)
