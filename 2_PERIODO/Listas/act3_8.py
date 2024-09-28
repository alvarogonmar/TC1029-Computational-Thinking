#Sublistas de pares e impares
#Escribe un porgama que pregunte cuantos elementos se agregaran a una lista
#Despues debe leer esa cantidad de datos e ingresarlos a la lista
#lUEGO DEBE CREAR 2 listas, una con los valores pares de la lista original y otra con los valores impares de la lista original

#Entrada
#La cantidad de datos que tendra la lista, los valores enteros para la lista

elem = int(input('Ingrese la cantidad de elementos de su lista: '))
lista_impares = []
lista_pares = []
lista = []
for i in range(elem):
    num = int(input('Ingrese el numero para incluirlo en la lista: '))
    lista.append(num)
    if num % 2 == 0:
        lista_pares.append(num)
    elif num % 2 != 0:
        lista_impares.append(num)
print(f'Lista original:\n {lista}')
print(f'Lista pares:\n {lista_pares}')
print(f'Lista impares:\n {lista_impares}')
