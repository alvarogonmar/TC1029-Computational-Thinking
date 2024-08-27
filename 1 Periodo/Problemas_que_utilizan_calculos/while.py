'''i = 0
while i <= 3:
    print(f'{i}: Hello')
    i=i+1

j = 4
while j >= 1:
     print(f'{j}: H1')
     j=j-1

#CICLO WHILE ANIDADO
h = 1
while h<=4:
    print('Python', end=' ')      #end (terminar en vacio, no pasa el cursor al sigueinte renglon)
    d=1
    while d<=3:
        print('ra', end=' ')
        d=d+1
    print('')
    h=h+1
     
#Ciclo while para validar entradas de usuario
v_entrada = float(input('Introduce un numero positivo: '))
while v_entrada <=0:
    print(f'El numero: {v_entrada} No es un numero positivo')
    v_entrada = float(input('Introduce un numero positivo: '))
print(f'El numero {v_entrada} SI es un numero positivo')

#Ciclo while para validar entradas del usuario
#if break

v_entrada = float(input('Introduce un numero positivo: '))

while v_entrada <=0:
    if v_entrada == 0:
        print(f'El numero: {v_entrada} No es valido')
        print('El programa termina')
        break
    print(f'El numero {v_entrada} NO es un numero positivo')
    v_entrada = float(input('Introduce un numero positivo: '))'''


'''v_entrada = float(input('Introduce un numero positivo: '))

while v_entrada <=0:
    if v_entrada == 0:
        print(f'El numero cero No es valido')
        v_entrada = float(input('Introduce un numero positivo: '))
        continue
    v_entrada = float(input('Introduce un numero positivo: '))
else:
    print(f'El numero {v_entrada} es un numero positivo')'''


#REALICE UN CICLO WHILE QUE IMPRIMA LOS NUMEROS DEL 10 AL 0. EN CUENTA REGRESVA
'''num = 10
while num >= 0:
    print(f'{num}')
    num = num - 1'''

#ESTABLEZCA UNA VARIABLE LLAMADA TOTAL EN 0 PARA EMPEZAR. GENERE UN CICLO EN EL QUE MIENRAS TOTAL ES DE 50  O MENOS PIDA AL USUARIO
#QUE INTRODUZCA UN NUMERO. SUME EL NUMERO INTRODUCIDO A TOTAL E IMPRIME EL MENSAJE. 'EL VALOR TOTAL' EL CICLO TERMINA CUANDO EL TOTAL SUPERE LOS 50

'''total = 0

while total <=50:
    numero = int(input('Introduzca un numero: '))
    total = total + numero
    print(f'{total}')'''


