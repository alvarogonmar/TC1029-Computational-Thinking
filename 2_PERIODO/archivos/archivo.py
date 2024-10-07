import pathlib

# Crear objeto Path a partir de una cadena
path1 = pathlib.Path('/Users/alvarogonzalez/Documents/ITC/1_Primer_Semestre/1ER_PERIODO/TC1029-Computational-Thinking/2_PERIODO/archivos/file1.txt')
print('El objeto Path: ')
print(path1)

# Usando los metodos Path.home() y Path.cwd()
home = pathlib.Path.home()
print('El directorio home: ')
print(home)

current = pathlib.Path.cwd()
print('El cwd es:')
print(current)