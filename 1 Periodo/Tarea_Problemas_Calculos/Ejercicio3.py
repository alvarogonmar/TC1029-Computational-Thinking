#Ejercicio 3.- Escriba un programa que convierta de grados a radianes.

#Con este programa podremos ser capaces de convertir "x" cantidad de grados
# en radianes mediante la fórmula

import math
grados = int(input('Ingrese el valor en grados: \r\n'))
radianes = (grados*math.pi)/180

print(f'La cantidad de: {grados} grados en radianes es igual a: {radianes}')