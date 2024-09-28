#Declarar una lista 2 formas:
lista = list() #constructor
lista1 = []
print(type(lista))
print(type(lista1))

#lista de enteros
lista = [2,3,4,5,34]

#lista de cadenas
lista1 = ['abc', 'xyz', 'dfg','lmn']

#lista con distitntos tipos de datos
lista2 = ['A', 234, 12, 'abc']

#Imprimir la longitud de una lista
print(len(lista))

#Crear lista apartir de otra secuencia
vlista=list('Python')
print(vlista)

print('*'*50)

#Creacion de lista con range
rang_lista=list(range(10))
print(rang_lista)

print('*'*50)

#Indice
lista2 = ['A', 234, 12, 'abc']
print(lista2[2])

print('*'*50)

#Indices negativos (del ultimo elemento al primero) 
lista2 = ['A', 234, 12, 'abc']
print(lista2[-1])

print('*'*50)

#Usando for
lista2 = ['A', 234, 12, 'abc']
for i in lista2:
    print(i)

print('*'*50)

num_elem = len(lista2)-1 #Obtener longitud de la lista (con -1 es para que de el ultimo elemento)
for x in range(num_elem,-1,-1): 
    print(lista2[x])

print('*'*50)

#Cambiar elementos de una lista
print(lista2)
lista2 = ['A', 234, 12, 'abc']
lista2[2]='Hello'
print(lista2)

print('*'*50)

#Slicing de listas
lista2 = ['A', 234, 12, 'abc']
print(lista2[1:3]) #imprime solo del indice 1 al 3
#indicar solo desde el indice que le ponga hasta el final
print(lista2[1:])
#Inicio hasta el indice 2
print(lista2[:2])

print('*'*50)

#Metodos con cadenas
v_list = ['a','d','c','k','e']
print(v_list) 
v_list.sort() #ordenar por alfabeto, mayor a menor
print(v_list)

print('*'*50)

v_list.sort(reverse=True) #orden descendente
print(v_list) 

print('*'*50)

#Metodo append() 
v_list.append('k') #permite agregar elemento al final de la lista
print(v_list)

print('*'*50)

#Metodo insert
v_list.insert(3, 'L') #poner primero el inidce(lo pone en el indice donde lo quiero poner), y despues el valor
print(v_list)

#Metodo pop
v_list = ['a','d','c','k','e']
print(v_list)
v_list.pop() #quita el ultimo eleento de la lista si no le pones indice
print(v_list)
print('*'*50)
#Especificando el indice
v_list = ['a','d','c','k','e']
print(v_list)
v_list.pop(1) #quita el  eleento de la lista 
print(v_list)