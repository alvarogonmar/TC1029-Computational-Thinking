# # Problema: Registro de Ventas de Productos
# # Descripción: Crea un programa que permita registrar las ventas de productos en una tienda. El programa debe permitir al usuario:

# # Agregar productos vendidos con su cantidad y precio.
# # Calcular el total de ingresos generados.
# # Guardar las ventas en un archivo de texto.
# # Requerimientos:

# # Usa un diccionario para almacenar el nombre del producto como clave, y una lista con la cantidad vendida y el precio como valor.
# # Permite ingresar varios productos en una misma sesión.
# # Calcula el total de ingresos multiplicando la cantidad vendida por el precio de cada producto.
# # Guarda las ventas en un archivo llamado ventas.txt.


def sold(sales):
    product = input('Product Sold: ')
    amount = int(input('Amount sold: '))
    price = float(input('Price: '))

    if product in sales:
        sales[product][0] += amount 
    else:
        sales[product] = [amount, price] 

def total(sales):
    total_amount = 0
    for product, information in sales.items():
        amount, price = information
        total_amount += amount * price
    return total_amount

def save_in_file(sales):
    try:
        with open('sales.txt', 'w') as file:
            for product, information in sales.items():
                amount, price = information
                file.write(f'Product: {product}, Amount: {amount}, Price: {price:.2f}\n')
            file.write(f'\nTotal: {total(sales):.2f}\n')  
        print('Sales saved in sales.txt')
    except Exception as e:
        print(f"Error saving file: {e}")

def manage_sales():
    sales = {}

    while True:
        option = int(input('\n1. Add a sale\n2. Show the total\n3. Save sales to file\n4. Exit\nChoose an option: '))

        if option == 1:
            sold(sales)
        elif option == 2:
            total_amount = total(sales) 
            print(f'Total: {total_amount:.2f}')
        elif option == 3:
            save_in_file(sales)
        elif option == 4:
            break
        else:
            print("Invalid option, please choose again.")

manage_sales()
