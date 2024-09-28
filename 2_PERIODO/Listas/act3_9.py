# RETO: Serie de fibonacci en una lista
# Diseña y codifica un programa que lea la cantidad de n elementos que desea tener en la lista.
# El programa debe validar que n sea mayor o igual que 0, de lo contrario lo vuelve a solicitar.
# Luego debe mostrar una lista que contenga los primeros n elementos de la serie de Fibonacci.
# Entrada
# Un número entero positivo que corresponde al número de términos de la serie de Fibonacci que queremos en la lista. 
# Si el dato recibido es menor que 0, se debe volver a solicitar


while True:
    elem = int(input('Ingrese la cantidad de elementos que desea en la lista: '))
    if elem < 0:
        print('Escriba un numero mayor o igual a 0')
        elem = int(input('Ingrese la cantidad de elementos que desea en la lista: '))
    else:
        fibonacci = []
        a, b = 0, 1
        for i in range(elem):
            fibonacci.append(a)  
            a, b = b, a + b 
        print(f'La lista hasta el elemento {elem} es:\n {fibonacci}')
        break
