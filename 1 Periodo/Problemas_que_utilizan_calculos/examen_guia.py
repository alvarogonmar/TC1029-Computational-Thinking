#USANDO EL CICLO WHILE (ANIDADOS) IMPRIMA UN SISTEMA DE COORDENADAS QUE INICIE EN (0,0) Y TERMINE EN (3,3). 
# LA IMPRESION EN PANTALLA DEBE SER DE LA SIGUIENTE MANERA
#(0,0)(0,1)(0,2)(0,3)
#(1,0)(1,1)(1,2)(1,3)
#(2,0)(2,1)(2,2)(2,3)
#(3,0)(3,1)(3,2)(3,3)
i = 0
while i < 4:
    j = 0
    while j < 4:
        print(f'({i},{j})', end='')
        j = j + 1
    i = i + 1
    print('')

print('')
print('*'*40)
print('')

for x in range(4):
    for y in range(4):
        print(f'({x},{y})', end='')
        y = y + 1
    x = x + 1
    print('')


#UTILIZANDO CICLOS, ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NUMERO ENTERO, SI EL NUMERO ES UN ENTERO MAYOR O IGUAL A DOS
#Y MENOR O IGUAL A 100 IMPRIMA EN PANTALLA UN TRIANGULO RECTANGULO COMO SE INDICA, DE LO CONTRARIO PIDE AL USUARIO INTRODUZCA UN NUEVO NUMERO
#*
#**
#***
#****
#*****
'''while True:
    num = int(input('Ingrese numero del 2-100\r\n'))
    i = 0

    if num < 2 or num > 100:
        print('Numero no valido')
        num = int(input('Ingrese numero del 2-100\r\n'))
    else:
        while i < num:
            i = i + 1
            print(f'*' * i)'''

'''num = 0

while num < 2 or num > 100:
    num = int(input('Introduzca su numero\r\n'))
for x in range(num+1):
    print(f'*'*x)'''

#UTILIZANDO CICLOS, ESCRIBIR UN PROGRAMA QUE PIDA AL USUARIO UN NUMERO ENTERO, SI EL NUMERO ES UN ENTERO MAYOR O IGUAL A DOS
#Y MENOR O IGUAL A 100 IMPRIMA EN PANTALLA COMO SE INDICA, DE LO CONTRARIO PIDE AL USUARIO INTRODUZCA UN NUEVO NUMERO


'''
while True:
    num = int(input('Ingrese su numero\r\n'))
    i = 0
    if num < 2 or num > 100:
        print('Numero no valido')
    else: 
        while i < num:
            i = i + 1
            print('*'*i)
        while i ==  num or i > 0:
            i = i - 1
            print('*'*i)'''

'''num = 0
while num < 2 or num > 100:
    num = int(input(('Introduzca un numero\r\n')))
for x in range(num+1):
    print(f'*'*x)
for x in range(num-1,0,-1):
        print(f'*'*x)'''

'''while True:
    word = input('Ingrese una palabra:\r\n').lower()
    if word == 'salir':
        break
    print(word)'''

'''num = int(input('Ingrese un numero\r\n'))

for i in range(1, num+1, 2):
    for j in range(i, 0, -2):
        print(j, end=' ')
    print('')'''

'''while True:
    num = int(input('Introduzca un numero del 2-100\r\n'))
    i = 1
    if num <2 or num > 100:
        print('numero no valido')
    else:
        while i<=num:
            print('*'*i)
            i += 1'''
