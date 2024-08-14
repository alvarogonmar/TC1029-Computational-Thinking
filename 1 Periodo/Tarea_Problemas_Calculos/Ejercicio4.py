#Ejercicio 4.- Escriba un programa que convierta de radianes a grados.
import math

radianes = 90
grados = (radianes*180)/math.pi

print(f'La cantidad de: {radianes} radianes en grados es igual a: {round(grados, 2)}')