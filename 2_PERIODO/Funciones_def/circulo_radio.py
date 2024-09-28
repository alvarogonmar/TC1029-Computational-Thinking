radio = int(input('Introduce el radio: '))

def area(radio):
    area = 3.14 * radio**2
    return area

print(f'El circulo de radio {radio} tiene un area del circulo es {area(radio)}')

# Genere una funcion que permita validar una entrada de datos. 
# La funcion debe solicitar un valor de tipo entero en un rango de 10 y 40. 
# Mientras el usuario no introduzca el valor solicitado siga pidiendo el valor

numero = 0
def num():
    numero = int(input('Introduzca un numero de 10 a 40: '))
    while numero < 10 or numero >= 40:
            numero = int(input('Introduzca un numero de 10 a 40: '))
num()

#Genere una funcion que reciba como argumento el radio de un circulo. 
# Dicha funcion debe calcular el area del circulo, e imprimir en pantalla: 
# El circulo de radio {valor del radio} tiene un area de: {valor del area}

def area(radio):
    area = 3.14 * radio**2
    print(f'El circulo de radio {radio_circulo} tiene un area de: {area}')

radio_circulo = int(input('Introduce tu radio: '))
area(radio_circulo)

#Genere una funcion que realice la multiplicacion de dos numeros que recibio como parametros. 
# La funcion debe imprimir los valores recibidos y el resultado de la multiplicacion
def multiplica(x,y):
    print('La multiplicacion de los numeros: ')
    print(f'{x} x {y} = {x*y}')

multiplica(4,3)

