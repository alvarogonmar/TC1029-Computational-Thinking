#Escribe un programa que pregunte cuantos elementos se agregaran a una lista
#Despues debe leer esa cantidad de datos e ingresarlos a la lista
#posteriormente debera construir una segunda lista, con el cuadrado de cada uno de los elementos de la lista original

#Entradas
#Un numero entero que representa la cantidad de numeros que contendra la lista 
#los numeros de la lista, enteros uno en cada renglon

elem = int(input('Introduzca el numero de elementos de su lista: '))
lista = []
for i in range(elem):
    num = int(input('Ingrese el numero que quiera al cuadrado: '))
    lista.append(num)
lista_cuadrado = []
for x in range(len(lista)):
    lista_cuadrado.append(lista[x] ** 2)
print(f'Los valores introducidos fueron:\n {lista}')
print(f'El cuadraro de cada valor de la anterior lista:\n {lista_cuadrado}')