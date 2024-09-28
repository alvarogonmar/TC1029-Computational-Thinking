#Suma dos listas por posicion
#Escribe un programa que permita realizar la suma elemento a elemento de dos listas de numeros enteros y con la msma cantidad de elementos

#Entrada
#Numero entero que indica cuantos elementos tendra cada lista. Numero debe ser > 0
#Los numeros enteros correspondientes a los elementos de cada una de las dos listas. Por ejemplo, si el usuairo tecle un 5
#Despues se deben leer 10 numeros, 5 para cada lista.

elem = int(input('Introduzca el numero de elementos de su lista: '))
lista1 = []
lista2 = []

for i in range(elem):
    num1 = int(input('Ingrese los numeros para su primera lista: '))
    lista1.append(num1)
for x in range(elem):
    num2 = int(input('Ingrese los numeros para su segunda lista: '))
    lista2.append(num2)

lista_sumas = []
for y in range(elem):
    lista_sumas.append(lista1[y]+lista2[y])

print(f'Lista 1\n {lista1}')
print(f'lista 2\n {lista2}')
print(f'Lista con la suma por posicion\n {lista_sumas}')
