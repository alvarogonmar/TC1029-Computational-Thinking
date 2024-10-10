# Contar pares e impares en una lista
# Escribe un programa que lea números en un rango de 0 y 2000 y los vaya agregando a una lista, 
# dejará de leer cuando se introduzca un número negativo. Luego el programa debe contar la cantidad de valores pares e impares de la lista. Considera al 0 como par.
# Entrada
# Cero o más valores enteros. Finaliza la captura con un número negativo. Nota que el número negativo no se debe agregar a la lista.

while True:
    numbers = int(input('Introduce numbers between 0-2000: '))
    if numbers < 0:
        print('Program Finished')
        break
    while numbers > 2000:
        numbers = int(input('Introduce numbers between 0-2000: '))

    even_numbers = 0
    odd_numbers = 0
    for i in range(numbers+1):
        if i % 2 == 0:
            even_numbers = even_numbers + 1
        else:
            odd_numbers = odd_numbers + 1
    print(f'Even numbers: {even_numbers}\n Odd numbers: {odd_numbers}')