from random import *
name = input('Say your name:\r\n')

print(f'So {name}, I chose one number between 1 - 100 and you have to discover it in 8 tries')

#Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
#un número que no está permitido.
# Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
#decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
#Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
#misma manera.
#Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
#intentos le ha tomado. 

number1 = randint(1,101)
life = 8
tries = 8-life

while life > 0:
    number2 = int(input('Number\r\n'))
    if number2 not in range(0,101):
        print('Please enter a number between 0-100')
    elif number2 < number1:
        print('Your number is smallest than the correct number')
        life -= 1
        print(f'{life} remaining attempts')
    elif number2 == number1:
        print('Your number is correct')
        break
        print(f'{life} remaining attempts')
    elif number2 > number1:
        print('Your number bigger than the correct number')
        life -= 1
        print(f'{life} remaining attempts')
if number2 != number1:
    print(f'Im sorry, you lose, the correct number was: {number1}')