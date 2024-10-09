#2
# Lee lista y muestra invertida
# Escribe un programa que pregunte cuántos elementos se agregarán a una lista. 
# Se debe validar que el número sea mayor que cero, si no lo es, se debe volver a pedir hasta que el usuario teclee un número positivo.

# Después debe leer esa cantidad de datos e ingresarlos a la lista.

# El programa debe desplegar los elementos ingresados en forma inversa, el indice mayor al menor, como se muestra en el ejemplo.

# Entradas
# Número entero n que corresponde al número de elementos a ingresar a la lista. 
# Debe ser mayor a 0 de lo contrario se solicitará de nuevo hasta que se cumpla la condición.
# Posteriormente se reciben los n elementos de la lista (números enteros), uno en cada renglón.

elements = int(input('Elements in the list: '))
while elements < 0:
    elements = int(input('Elements in the list: '))

list1 = []
for i in range(elements):
    numbers = (input(f'Introduce the number {i+1}: '))
    list1.append(numbers)
list1.sort(reverse=True)
for i in range(len(list1)):
    print(f'List [{len(list1)-1-i}]: {list1[i]}')
