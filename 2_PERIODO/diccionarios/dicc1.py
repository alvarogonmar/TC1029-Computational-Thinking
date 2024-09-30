#DECLARAR UN DICCIONARIO CON DATOS
capitales = {'Jalisco':'Guadalajara', 'Colima':'Colima', 'Michoacan':'Zamora'}
cobinados = {1:'Uno', 'Dos': 2.43, -3:[1,2,3]}

print(capitales)
print(cobinados)
print('*'*50)

#Imprimir la valor atreves de la llave
print(capitales['Jalisco'])
print('*'*50)

#VERIFICAR LA PERTENENCIA DE UNA LLAVE EN EL DICCIONARIO
capitales = {'Jalisco':'Guadalajara', 'Colima':'Colima', 'Michoacan':'Zamora'}
print('Mexico' in capitales) #operador de petenencia
print('Mexico' not in capitales) #operador de no pertenencia
print('*'*50)

#AGREGAR ELEMENTOS AL DICCIONARIO
print(capitales)
capitales['Yucatan'] = 'Merida'
print(capitales)
print('*'*50)

#CAMBIAR LLAVES QUE YA EXISTEN
print(capitales)
capitales['Colima'] = 'Manzanillo'
print(capitales)
print('*'*50)

#Eliminar elementos de un diccionario
capitales = {'Jalisco':'Guadalajara', 'Colima':'Colima', 'Michoacan':'Zamora'}
print(capitales)

#1. Utilizando el keyword del:
del capitales['Jalisco']

#2. Utilizando el metodo pop() NOS RETORNA EL VALOR
capitales.pop('Colima')
print(capitales)
print('*'*50)

#CICLO FOR CON DICCIONARIOS
capitales = {'Jalisco':'Guadalajara', 'Colima':'Colima', 'Michoacan':'Zamora'}
for llave in capitales:
    print(llave)
print('*'*50)

print(capitales.keys()) #DEVOLVER SOLO LAS LLAVES
for key in capitales.keys():
    print(key)
print('*'*50)

print(capitales.values()) #DEVOLVER SOLO LOS VALORES
for value in capitales.values():
    print(value)

