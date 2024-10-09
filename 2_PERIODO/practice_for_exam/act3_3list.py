#3
# Escribe un programa que lea un valor entero n, y después n valores enteros y los agregue a una lista.

# El programa debe calcular el promedio de los valores de la lista

# Finalmente debe mostrar la lista y en el siguiente renglón el promedio de los valores que contiene.

# Entradas

# Número entero n que corresponde al número de elementos a ingresar a la lista. 
# Debe ser mayor a 0 de lo contrario se solicitará de nuevo hasta que se cumpla la condición.

# Posteriormente se reciben los n elementos de la lista, uno en cada renglón.

elements = int(input('Elements in the list: '))
while elements < 0:
    elements = int(input('Elements in the list: '))
list1 = []
for i in range(elements):
    numbers = int(input(f'Introduce the number {i+1}: '))
    list1.append(numbers)

average = sum(list1) / len(list1)
print(list1)
print(average)