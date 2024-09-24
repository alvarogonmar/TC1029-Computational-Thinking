#Desarrolla un programa que contenga las siguientes funciones:
#una función llamada area_cilindro, que reciba el radio y altura del cilindro y retorne el área calculada.
#una función llamada volumen_cilindro, que reciba el radio y altura del cilindro y regrese el volumen calculado.
#El programa debe leer el radio y la altura de un cilindro, luego llamar a las funciones y finalmente mostrar el área y volumen del cilindro.

#Entrada
#El radio del cilindro
#La altura del cilindro

radio = float(input('Introduzca el radio: '))
altura = float(input('Introduzca la altura: '))

def area_cilindro(radio, altura):
    area = round(((2*3.14*radio*altura) + 2*3.14*radio**2),2)
    return area

def volumen_cilindro(radio, altura):
    volumen = round(((3.14*radio**2) * altura),2)
    return volumen

area = area_cilindro(radio, altura)
volumen = volumen_cilindro(radio, altura)

print(f'El area del cilindro es: {area}')
print(f'El volumen del cilindro es: {volumen}')