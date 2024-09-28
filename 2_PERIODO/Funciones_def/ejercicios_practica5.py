def es_bisiesto(año):
    if año % 400 == 0:
        return 'Es bisiesto'
    elif año % 4 == 0 and año % 100 != 0:
        return 'Es bisisesto'
    else:
        return 'No es bisiesto'

año = int(input('Introduce un año: '))

resultado = es_bisiesto(año)
print(f"El año {año} {resultado}.")