#3
# Escribe un programa que lea un valor entero n, y después n valores enteros y los agregue a una lista.

# El programa debe calcular el promedio de los valores de la lista

# Finalmente debe mostrar la lista y en el siguiente renglón el promedio de los valores que contiene.

# Entradas

# Número entero n que corresponde al número de elementos a ingresar a la lista. 
# Debe ser mayor a 0 de lo contrario se solicitará de nuevo hasta que se cumpla la condición.

# Posteriormente se reciben los n elementos de la lista, uno en cada renglón.

# while n <= 0:
#     n = int(input('Numero de elementos que desea agregar a la lista: '))
# lista = []
# for i in range(n):
#         lista.append(i+1)
#         print(lista)
n = int(input('Numero de elementos que desea agregar a la lista: '))

while n <= 0:
    n = int(input('Numero de elementos que desea agregar a la lista: '))
lista = []
for i in range(n):
        num = int(input(f'Ingrese el elemento {i+1}: '))
        lista.append(num)
promedio = sum(lista) / len(lista)

print(lista)
print(promedio)
