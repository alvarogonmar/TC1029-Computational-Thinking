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
path = current / 'archivos' / 'ejemplo.txt'
print(f'El path nuevo formado es \n {path}')

# Usando atributos de la clase Path:
# Atributo name
# Retorna el nombre del archivo o directorio al que apunta el objeto Path
print(f'home: {home.name}')
print(f'current: {current.name}')
print(f'path: {path.name}')

# Usando atributos de la clase:
# atributo stem y suffix
print(f'El nombre del archivo es {path.stem}')
print(f'La extencion del archivo es: {path.suffix}')

# Usando atributos de la clase Path:
# Atributo parents:
# Retorna una secuencia con los directorios padre del archivo
parents_Directory = list(path.parents)
# print(f'Parents Directory: {parents_Directory}')

for element in parents_Directory:
    print(element)

# Metodos sobre la clase Path
# Usando el meodo exists
ruta = (path.exists())
print(f'La ruta indicada existe?: {ruta}')

# Verificar si la rula se refiere a un archivo o a un directorio
file = (path.is_file())
print(f'El path apunta a un archivo?: {file}')

directory = (current.is_dir())
print(f'El objeto apunta a un directorio?: {directory}')

# Crear una nueva carpeta
new_dir = current /'New_Folder'
new_dir.mkdir(exist_ok= True)

# Algo equivalente
if not new_dir.exists():
    new_dir.mkdir()

# Crear un nuevo archivo
# new_dir = current / 'Carpeta nueva'
new_file = new_dir / 'New_File.txt'
new_file.touch() #make a new file
