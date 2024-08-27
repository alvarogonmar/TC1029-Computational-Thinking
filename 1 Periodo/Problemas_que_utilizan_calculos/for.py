'''for x in range(6):
    print(x)

#REALICE UN PORGRAMA QUE SOLICITE AL USUARIO SU NOMBRE Y MEDIANTE UN CICLO FOR
#IMPRIMA TRES VECES EL NOMBRE DEL USUARIO.

nombre = input('Ingrese su nombre\r\n')
for x in range(0,3):
    print(nombre)

#SOLICITE AL USAIRO INTRODUZCA UN NUMERO ENTRE 1 Y 12. LUEGO USANDO UN CICLO FOR IMPRIMA
#LA TABLE DE MULTIPLICAR DE DICHO NUMER INTRODUCIDO. 

num = int(input('Introduzca un numero del 1-12\r\n'))

for x in range(1-13):
    mul = x * num
    print(f'{x}*{num}: {mul}')


#CADENA
var_cad = 'Muy buen dia'
for elem in var_cad:
    print('El ciclo se repite')

#CADENA VERTICAL
for elemento in 'Muy buen dia':
    print(elemento)'''

#CICLO FOR CADENA CON ELEMENTO ITERABLE
contador = 0
for i in 'Buen dia':
    print(f'{contador}.- {i}')
    contador += 1

#SOLICITE AL USUARIO SU NOMBRE E IMPRIMA UNA LETRA POR CADA LINEA UTILIZANDO UN CICLO FOR
nombre = input('Ingrese su nombre\r\n')

for i in nombre:
    print(i)