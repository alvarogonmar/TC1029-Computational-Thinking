# 1. Problema 1: Agenda de Contactos (Fácil-Medio)
# Descripción: Crea un programa que permita almacenar y gestionar una agenda de contactos. 
# El programa deberá permitir al usuario agregar, buscar y mostrar contactos, 
# utilizando un diccionario donde las llaves sean los nombres y los valores sean los números de teléfono.

# Requerimientos:

# La función principal debe solicitar al usuario que elija una opción: agregar, buscar o mostrar contactos.
# Al agregar un contacto, el usuario debe ingresar el nombre y el número de teléfono, que se guardarán en un diccionario.
# Al buscar un contacto, el programa deberá solicitar el nombre y mostrar el número si está en la agenda.
# Al mostrar, se deben listar todos los contactos almacenados.

def add_contact(contacts):
    name = input('Name of the new contact: ')
    number = int(input('Number of your new contact: '))
    contacts[name] = number

def find_contact(contacts):
    name = input('Name of the contact to find: ')
    if name in contacts:
        print(f'{name}: {contacts[name]}')
    else:
        print('Contact not found')

def show_contact(contacts):
    if contacts:
        for name, number in contacts.items():
            print(f'{name}: {number}')
    else:
        print('You have 0 contacts')

def contacts_list():
    list1 = {}
    while True:
        option = int(input("\n1. Add new contact\n2. Find contact\n3. Show contacts\n4. Leave:\n"))
        if option == 1:
            add_contact(list1)
        elif option == 2:
            find_contact(list1)
        elif option == 3:
            show_contact(list1)
        elif option == 4:
            break

contacts_list()