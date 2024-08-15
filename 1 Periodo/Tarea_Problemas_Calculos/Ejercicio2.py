#Ejercicio 2.- Escriba un programa para calcular el área de un trapecio.

#Este programa está hecho para calcular el área de un trapecio,
# conociendo su altura, base menor y base mayor, tendremos el resultado del área mediante su fórmula


altura = int(input('Ingrese el valor de la altura: \r\n'))
base_menor = int(input('Ingrese el valor de la base menor: \r\n'))
base_mayor = int(input('Ingrese el valor de la base mayor: \r\n'))

area = ((base_mayor*base_menor*altura)/2)
print(f'El área del trapecio es igual a: {round(area, 2)}')