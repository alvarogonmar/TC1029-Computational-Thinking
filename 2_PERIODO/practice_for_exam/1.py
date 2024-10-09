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

def  fun_operations(a, b=2, op=''):
    if op == '+':
        addition = a + b
        print('The chosen operation is:  addition')
        print(f'The result of addition {a}+{b} = {addition}')
    elif op == '-':
        subtraction = a - b
        print('The chosen operation is: subtraction')
        print(f'The result of subtraction {a}-{b} = {subtraction}')
    elif op == '*':
        multiplication = a * b
        print('The chosen operation is: multiplication')
        print(f'The result of multiplication {a}*{b} = {multiplication}')
    elif op == '/':
        division = a / b
        print('The chosen operation is: division')
        print(f'The result of the division {a}/{b} = {division}')
    elif op == '**':
        power = a ** b
        print('The chosen operation is: power')
        print(f'The result of the power {a}**{b} = {power}')
    elif op == '%':
        residue = a % b
        print('The chosen operation is: residue')
        print(f'The result of the residue {a}%{b} = {residue}')

fun_operations()