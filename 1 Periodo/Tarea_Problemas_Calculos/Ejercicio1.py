#Ejercicio 1.- Escriba un programa que calcule el área de la superficie y el volumen de un cilindro.

#Este programa lo que realizará es calcular el área de la superficie y el volumen de un cilindro, 

import math

#Variables
radio = 5
altura = radio*2
math.pi


area_lateral = 2 * math.pi * radio * altura
area_bases = 2 * math.pi * (radio**2)
area_total = area_lateral + area_bases

volumen = math.pi * (radio**2) * altura


print(f'El área total de la superficie del cilindro es: {round(area_total, 2)} y el volumen es: {round(volumen, 2)}')
