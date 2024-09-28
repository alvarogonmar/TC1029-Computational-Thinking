#Realiza una función llamada funOperaciones que tenga un parámetro llamado a, un parámetro por default a 2 llamado b,
#y un parámetro llamado op que indique mediante el operador aritmético recibido la operación aritmética a realizar. 
#La función permite hacer una de las siguientes operaciones aritméticas: suma, resta, multiplicación, división, residuo o potencia, 
# entre los parámetro a y b según el operador que reciba. 
# Además la función no debe permitir realizar operación de residuo o división si b es cero y debe indicar: 
# Error División Sobre Zero.
#Por ejemplo, si se realiza el siguiente llamado a ejecución de la función esto es lo que imprimiría:
#funOperaciones(12,3, "%")
#La operación elegida es: Residuo
#Al ejecutar la operación se obtiene: 12 % 3 = 0
#Al final pega tu código aquí, no olvides que debe estar bien identado y en la sintaxis adecuada de python

def funOperaciones(a, b=2, op=''):
    if op == '+':
        print('La operacion elegida es: Suma')
        suma = a + b
        print(f'Al ejecutar la operación se obtiene: {a}{op}{b} = {suma} ')
    elif op == '-':
        print('La operacion elegida es: Resta')
        resta = a - b
        print(f'Al ejecutar la operación se obtiene: {a}{op}{b} = {resta} ')

    elif op == '*':
        print('La operacion elegida es: Multiplicacion')
        mult = a * b
        print(f'Al ejecutar la operación se obtiene: {a}{op}{b} = {mult} ')
    elif op == '/':
        if b != 0:
            print('La operacion elegida es: Division')
            div = a / b
            print(f'Al ejecutar la operación se obtiene: {a}{op}{b} = {div} ')
        else:
            print('Error División Sobre Zero')
    elif op == '%':
        if b != 0:
            print('La operacion elegida es: Residuo')
            residuo = a / b
            print(f'Al ejecutar la operación se obtiene: {a}{op}{b} = {residuo} ')
        else:
            print('Error División Sobre Zero')
    elif op == '**':
        print('La operacion elegida es: Potencia')
        potencia = a ** b
        print(potencia)
        print(f'Al ejecutar la operación se obtiene: {a}{op}{b} = {potencia} ')











