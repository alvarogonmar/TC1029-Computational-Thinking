# Escribe un programa que pregunte cuántos elementos se agregarán a una lista. 
# Se debe validar que el número sea mayor que cero, si no lo es, se debe volver a pedir hasta que el usuario teclee un número positivo.

# Después debe leer esa cantidad de datos e ingresarlos a la lista.

# Finalmente mostrar la lista leída en el formato que se muestra en el ejemplo. 

# Entradas

# Número entero n que corresponde al número de elementos a ingresar a la lista. 
# Debe ser mayor a 0 de lo contrario se solicitará de nuevo hasta que se cumpla la condición.
# Posteriormente se reciben los n elementos de la lista, uno en cada renglón

elem = int(input('Numero de elementos que desea agregar a la lista: '))
while elem <= 0:
    elem = int(input('Numero de elementos que desea agregar a la lista: '))
lista = []
for i in range(elem):
        num = input(f"Ingrese el elemento {i+1}: ")
        lista.append(num)
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")
