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

num1 = 28
num2 = 3.5

print(f'La suma del numero 1 y el numero 2 da un total de {num1+num2}')
print(f'La resta del numero 1 y el numero 2 da un total de {num1-num2}')
print(f'La multiplicacion del numero 1 y el numero 2 da un total de {num1*num2}')
print(f'La division del numero 1 y el numero 2 da un total de {num1/num2}')
print(f'La potencia del numero 1 y el numero 2 da un total de {num1**num2}')
print(f'La residuo del numero 1 y el numero 2 da un total de {num1%num2}')

#DECLARE UNA VARIABLE ENTERA Y ASIGNE VALOR DE 2
#dECLARE UNA VAIRBALE DE TIPO FLOTANTE Y ASIGENE EL VALOR DE PI CON 4 DECIMALES DE PRECISION
#DECLARE UNA VAIRABLE LLAMADA RADIO CON EL VALOR DE 4.76
#UTILIZANDO LAS VARIABLES ANTERIORMENTE DECLARADAS FORMULE LAS EXPRESIONES PARA CALCULAR EL PERIMETRO Y EL AREA DE UN CIRCULO
#UTILLICE f-string PARA IMRPIMIR. NO OLVIDE PROPORCIONAR SUFICIENTE INFORMACION AL USUARIO

var_int = 2
var_float = 3.1416
radio = 4.76
perimetro = (var_float*(radio*2))
area = (var_float*4.76**2)
print(f'El perimetro es {perimetro} y el area del circulo es de {area}')