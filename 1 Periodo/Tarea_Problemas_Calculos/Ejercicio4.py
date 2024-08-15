#Ejercicio 4.- Escriba un programa que convierta de radianes a grados.

#Con este programa podremos ser capaces de convertir "x" cantidad de radianes
# en grados mediante la fórmula

import math

radianes = int(input('Ingrese el valor en radianes: \r\n'))
grados = (radianes*180)/math.pi

print(f'La cantidad de: {radianes} radianes en grados es igual a: {round(grados, 2)}')