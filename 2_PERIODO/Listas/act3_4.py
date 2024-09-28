# Contar pares e impares en una lista
# Escribe un programa que lea números en un rango de 0 y 2000 y los vaya agregando a una lista, 
# dejará de leer cuando se introduzca un número negativo. Luego el programa debe contar la cantidad de valores pares e impares de la lista. Considera al 0 como par.
# Entrada
# Cero o más valores enteros. Finaliza la captura con un número negativo. Nota que el número negativo no se debe agregar a la lista.

while True:
    num = int(input('Introduce un numero del 0-2000, te dire cuantos numeros pares e impares hay desde 0 hasta tu numero: '))
    if num < 0:
        print('Fin del programa')
        break
    while num > 2000:
        num = int(input('Introduce un numero del 0-2000, te dire cuantos numeros pares e impares hay desde 0 hasta tu numero: '))
    pares=0
    impares=0
    for i in range(num+1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f'Numero de pares {pares}')
    print(f'Numero de impares {impares}')