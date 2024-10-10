# Problema: Registro de Ventas de Productos
# Descripción: Crea un programa que permita registrar las ventas de productos en una tienda. El programa debe permitir al usuario:

# Agregar productos vendidos con su cantidad y precio.
# Calcular el total de ingresos generados.
# Guardar las ventas en un archivo de texto.
# Requerimientos:

# Usa un diccionario para almacenar el nombre del producto como clave, y una lista con la cantidad vendida y el precio como valor.
# Permite ingresar varios productos en una misma sesión.
# Calcula el total de ingresos multiplicando la cantidad vendida por el precio de cada producto.
# Guarda las ventas en un archivo llamado ventas.txt.

def sold(sales):
    product = input('Product Sold: ')
    amount = int(input('Amount sold: '))
    price = float(input('Price: '))

    if product in sales:
        sales[product][0] += amount
    else:
        sales[product] = [amount, price]

