#Declare una funcon que imprima el pais de origen, 
# La funcion debe tener un parametro por default de tipo cadena, el cual debe estar inicializando con el valor “Mexico”. 
# La funcion debe imprimir Yo soy de {valor}

def funcDeDondeSoy(estado, pais='Mexico'):
    print(f'Yo soy de: {pais}'
          f'\ndel estado de: {estado}')


#funcDeDondeSoy()
funcDeDondeSoy('Japon')