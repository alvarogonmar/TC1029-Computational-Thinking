#Un coche se encuentra en el centro de una pista circular de 100 metros de radio. 
#Desde su posicion inicial, el coche se desplaza 100 metros en linea recta
#formando un angulo de 60° con respecto a una linea imaginaria que conecta el centro de la pista con un la horizontal x positiva.

#Calcula la distancia horizontal y vertical desde el punto de referencia en la pista hasta el punto de llegada del coche a la pista.
#Encuentra la raiz cuadrada del area total de la pista circular.
#Verifica la relacion entre las distancias horizontal y vertical utilizando tangente del angulo

import math

#informacion
radio = 100
angulo_grados = 60
angulo_radianes = math.radians(angulo_grados)

#Distanca horizontal y vertical
distancia_horizontal = radio * math.cos(angulo_radianes)
distancia_vertical = radio * math.sin(angulo_radianes)

#Raíz cuadrada del área de la pista circular
area = math.pi * radio**2
area_raiz = math.sqrt(area)
#Calculo de la relacion entre distancias horizontal y vertical
relacion_distancias = round(distancia_vertical/distancia_horizontal, 2)


print(f'La distancia horizontal desde el centro de la pista es de {round(distancia_horizontal, 2)}')
print(f'La distancia vertical desde el centro de la pista es de {round(distancia_vertical, 2)}')
print(f'La raiz cuadrada del total del area es de {round(area_raiz,3)}')
print(f'''El resultado de la division de la distancia vertical entre la horizontal es de {relacion_distancias}\n
      y la tangente del angulo 60 es {round(math.tan(angulo_radianes), 2)}''')
