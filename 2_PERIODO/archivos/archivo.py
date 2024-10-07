import pathlib

# Crear objeto Path a partir de una cadena
path1 = pathlib.Path('/Users/alvarogonzalez/Documents/ITC/1_Primer_Semestre/1ER_PERIODO/TC1029-Computational-Thinking/2_PERIODO/archivos/file1.txt')
print('El objeto Path: ')
print(path1)

# Usando los metodos Path.home() y Path.cwd() (current working directory)
home = pathlib.Path.home()
print('El directorio home: ')
print(home)

current = pathlib.Path.cwd()
print('El cwd es:')
print(current)

# Usando el operador diagonal
path = current / 'ejemplo.txt'
print(f'El path nuevo formado es \n {path}')

# Usando atributos de la clase Path:
# Atributo name
# Retorna el nombre del archivo o directorio al que apunta el objeto Path
print(f'home: {home.name}')
print(f'current: {current.name}')
print(f'path: {path.name}')
