#Desarrolla un programa que contenga las siguientes funciones:
#una función llamada area_cilindro, que reciba el radio y altura del cilindro y retorne el área calculada.
#una función llamada volumen_cilindro, que reciba el radio y altura del cilindro y regrese el volumen calculado.
#El programa debe leer el radio y la altura de un cilindro, luego llamar a las funciones y finalmente mostrar el área y volumen del cilindro.

#Entrada
#El radio del cilindro
#La altura del cilindro

def cylinder_area(radio, height):
    area = round(((2*3.14*radio*height) + 2*3.14*radio**2),2)
    return area
def cylinder_volume(radio, height):
    volume = round(((3.14*radio**2) * height),2)
    return volume

radio = float(input('Radio: '))
height = float(input('Height: '))

print(f'The cylinder area is: {cylinder_area(radio=radio, height=height)}')
print(f'The cylinder volume is: {cylinder_volume(radio=radio, height=height)}')
