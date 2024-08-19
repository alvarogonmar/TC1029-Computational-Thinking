'''print('hello world')

#Variables

#Create int
var_entera = 1234

#float
var_flotante = 4.4

#complex
var_complex = -5j

#print
print(f'El valor de la variable var_entera es: "{var_entera}"')

#type
print(type(var_flotante))

#id
print('Lo siguiente son las direcciones fisicas de los datos almacenados')
print(id(var_complex))
print(id(var_flotante))
print(id(var_entera))


#Operadores aritmeticos
print(3+3)
v_1 = 45
v_2 =30

print(f'El resultado de multiplicar v_1 y v_2 es: "{v_1*v_2}"')'''


#DECLARA 2 VARIABLES NUM1 Y NUM2, asigne los valores 28 y 3.5. 
#Realice cada una de las operaciones especificadas anteriormente. Use f-strings
'''
num1 = 28
num2 = 3.5

print(f'La suma del numero 1 y el numero 2 da un total de {num1+num2}')
print(f'La resta del numero 1 y el numero 2 da un total de {num1-num2}')
print(f'La multiplicacion del numero 1 y el numero 2 da un total de {num1*num2}')
print(f'La division del numero 1 y el numero 2 da un total de {num1/num2}')
print(f'La potencia del numero 1 y el numero 2 da un total de {num1**num2}')
print(f'La residuo del numero 1 y el numero 2 da un total de {num1%num2}')'''

#DECLARE UNA VARIABLE ENTERA Y ASIGNE VALOR DE 2
#dECLARE UNA VAIRBALE DE TIPO FLOTANTE Y ASIGENE EL VALOR DE PI CON 4 DECIMALES DE PRECISION
#DECLARE UNA VAIRABLE LLAMADA RADIO CON EL VALOR DE 4.76
#UTILIZANDO LAS VARIABLES ANTERIORMENTE DECLARADAS FORMULE LAS EXPRESIONES PARA CALCULAR EL PERIMETRO Y EL AREA DE UN CIRCULO
#UTILLICE f-string PARA IMRPIMIR. NO OLVIDE PROPORCIONAR SUFICIENTE INFORMACION AL USUARIO

'''var_int = 2
var_float = 3.1416
radio = 4.76
perimetro = (var_float*(radio*2))
area = (var_float*4.76**2)
print(f'El perimetro es {perimetro} y el area del circulo es de {area}')'''


#input

#Realice un programa que solicite la edad del usuario e imprima el resultado de sumarle dos a la edad 

'''edad = int(input('Ingrese su edad solamente en numero: \r\n'))

print(f'Tu edad en dos años va a ser {edad + 2} años')'''


#CASTING
'''a = '123'
b = int(a)
print(type(b)) #entero
print(type(a)) #cadena

c = float(a)
print(type(c)) #float'''

#Cambiar float a int
'''a = '123.44'
b = float(a)
c = int(b)

print(type(c))'''


#EJERCICIO
#Solicite al usuario indtroduzca un numero entero o flotante, y realice las siguientes operaciones
#Eleve al cuadrado el valor dado e imprima el resultado usando f-strings 
# (en la impresion indique el valor de la variable, la operacion que se realiza y el resultado)

#Obtenga la operacion modulo del valor proporcionado sobre 2 e imprima el resultado usando f-strings 
# (En la impresion indique el valor de la variable, la operacion que se realiza y el resultado)

'''numero = int(input('Ingrese el numero entero: \r\n'))
numero_cuadrado = numero**2
print(f'El numero {numero} elevado al cuadrado es: {numero_cuadrado}')

residuo = numero%2
print(f'El residuo de su numero dividido entre 2 es: {residuo}')'''
'''
varUno = -23.34
print(abs(varUno))
print(f'El valor {varUno} en valor absoluto es {abs(varUno)}')'''

'''import math

print(round(math.pi, 2))

#Booleanos
print(type(True))
print(type(False))


#Expresiones condicionales
a = 5
b = -12
print(a>b)
print(b==40)
print(a<=b and b!=0)'''

'''#if
calif = 87
if calif >= 70:
    print('Pasaste la materia')
else:
    print('No pasaste la materia')

calif = 60
if calif >= 70:
    print('Pasaste la materia')
else:
    print('No pasaste la materia')

calif = 97
if calif >= 95:
    print('Exelente')
elif calif >= 70:
    print('Pasaste la materia)
else:
    print('No pasaste)

#REALICE UN PROGRAMA QUE SOLICITE AL USUARIO SU EDAD Y HAGA:
#Si su edad es mayor a 20 anios diga : El tiempo no espera a nadie
#Realice UN PROGRAMA QUE SOLICITE AL USUARIO INTRDUZCA EL DIA DE LA SEMANA. SI EL DIA ES VIERNES INDIQUE YA ES FIN DE SEMANA

edad = int(input('Ingrese su edad: \n\r'))

if edad > 20:
    print('El tiempo no espera a nadie')


dia = (input('Que dia es hoy?: \n\r')).lower()

if dia == 'viernes':
    print('Ya es fin de semana')'''


#REALIE UN PROGRAMA QUE SOLICITE UN NUMERO AL USUARIO EN UN RANGO DE 0 A 20. SI EL USUARIO INSTRODUCE UN NUMERO MAYOR A 20 IMRPRIMA "EL VALOR ES MUY ALTO"
#sI NO GRACIAS

numero = int(input('Introduzca un numero de 0-20\n\r'))
if numero >= 21:
    print('El valor es muy alto')
else:
    print('Gracias')

#REALICE UN PROGRAMA QUE SOLICITE AL USAURIO INTRODUZCA EL DIA DE LA SEMANA, SI EL DIA INTRODUCIDO ES VIERNES INDIQUE YA ES FIN DE SEMANA. EN CASO
#DE CUALQUIER OTRO DIA INDIQUE QUE TENGA UN BUEN DIA

dia = input('Introduzca el dia de la semana\n\r').lower()

if dia == 'viernes':
    print('Ya es fin de semana')
else:
    print('Que tenga buen dia')

#HAGA UN PROGRAMA QUE SOLICITE DOS NUMEROS AL USUARIO. SI EL PRIMER NUMERO ES MAYOR QUE EL SEGUNDO IMPRIMA PRIMERO EL SEGUNDO NUMERO INTRODUCIDO SEGUIOD DEL
#PRIER NUMERO SEPARADOS POR UN GUION. EN CASO CONTRARIO IPRIMA EN EL ORDEN INVERSO AL ANTERIOR CASO
num1 = int(input('Ingrese el numero 1\n\r'))
num2 = int(input('Ingrese el numero 2\n\r'))

if num1 > num2:
    print(f'{num2}-{num1}')
else:
    print(f'{num1}-{num2}')

#REALICE UN PROGRAMA QUE SOLICITE AL USUARIO SU COLOR FAVORITO, SI EL COLOR ES ROJO DEVUELVA EL MENSAJE A MI TAAMBIEN ME GUSTA EL ROJO. 
#DE LO CONTRARIO DESPLIEGUE A MI NO ME GUSTA EL COLOR {} YO PREFIERO EL ROJO

color = input('Dime tu color favorito\n\r').lower()

if color == 'rojo':
    print('A mi tambien me gusta el rojo')
else:
    print(f'A mi no me gusta el color {color}, me gusta mas el rojo')