#Escriba un programa que solicite un número entero al usuario, e indique si el número es:
#Par positivo
#Impar positivo
#Par negativo
#Impar negativo



'''while True:
    numero = int(input('Ingrese un numero entero\r\n'))

    if numero > 0 and numero % 2 == 0:
        print('Tu numero es par positivo')

    elif numero > 0 and numero % 2 != 0:
        print('Tu numero es impar positivo')

    elif numero < 0 and numero % 2 == 0:
            print('Tu numero es par negativo')

    elif numero < 0 and numero % 2 != 0:
        print('Tu numero es negativo impar')
    else:
         print('Numero no valido')'''



#2DA OPCION

'''while True:
    numero = int(input('Ingrese un numero entero\r\n'))
    if numero > 0:
        if numero % 2 == 0:
              print('Tu numero es par positivo')
        else:
            print('Tu numero es impar positivo')
    if numero < 0:
        if numero % 2 == 0:
            print('Tu numero es par negativo')
        else: 
            print('Tu numero es negativo impar')
'''

#REALICE UN PROGRAMA QUE INDIQUE CUAL ES EL MAYOR DE 3 NUMEROS ENTEROS x, y, z PROPORCIONADOS POR EL USUARIO, NO USES PYTHON MAX()

'''x = int(input('Numero 1\r\n'))
y = int(input('Numero 2\r\n'))
z = int(input('Numero 3\r\n'))

if x > y and x > z:
    print(f'El numero mayor es {x}')
elif y > x and y > z:
    print(f'El numero mayor es {y}')
else:
    print(f'EL numero mayor es {z} ')'''


#USANDO EL CICLO WHILE (ANIDADOS) IMPRIMA UN SISTEMA DE COORDENADAS QUE INICIE EN (0,0) Y TERMINE EN (3,3). LA IMPRESION EN PANTALLA DEBE SER DE LA SIGUIENTE MANERA

'''i = 0 #PARA ABAJO
while i < 4:
    j = 0 # A LA DERECHA
    while j < 4:
        print(f'({i}, {j})', end='')
        j = j + 1
    print('')
    i = i + 1'''

'''for i in range(4):
    for j in range(4):
        print(f'({i}, {j}) ', end='')
    print('')'''

#UTILIZANDO CICLOS, ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NUMERO ENTERO, SI EL NUMERO ES UN ENTERO MAYOR O IGUAL A DOS
#Y MENOR O IGUAL A 100 IMPRIMA EN PANTALLA UN TRIANGULO RECTANGULO COMO SE INDICA, DE LO CONTRARIO PIDE AL USUARIO INTRODUZCA UN NUEVO NUMERO

'''while True:
    num = int(input('Introduzca el numero de 2-100\r\n'))
    i = 0
    if num < 2 or num > 100:
        print('Introduzca un numero valido')
    else:
        while i < num:
            i = i + 1
            print(f'*' * i)'''

'''
num = 0
while num < 2 or num > 100:
    num = int(input('Introduzca un numero del 2-100\r\n'))
for x in range(num + 1):
    for y in range(x):
        print('*', end='')
    print()'''

#UTILIZANDO CICLOS, ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NUMERO ENTERO, SI EL NUMERO ES UN ENTERO MAYOR O IGUAL A DOS
#Y MENOR O IGUAL A 100 IMPRIMA EN PANTALLA COMO SE INDICA, DE LO CONTRARIO PIDE AL USUARIO INTRODUZCA UN NUEVO NUMERO

while True:
    num = int(input('Introduzca el numero de 2-100\r\n'))
    i = 0
    if num < 2 or num > 100:
        print('Introduzca un numero valido')
    else:
        while i < num:
            i = i + 1
            print(f'*' * i)
        while i == num or i > 0:
            i = i - 1
            print(f'*' * i)

            

