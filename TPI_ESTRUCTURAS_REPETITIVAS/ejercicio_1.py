

# 1. Pedir nombre del cliente (solo letras y no vacío)
nombre = input("Cliente: ").strip()
while not nombre.isalpha():
    print("Error: El nombre debe contener solo letras y no estar vacío.")
    nombre = input("Cliente: ").strip()

# 2. Pedir cantidad de productos (entero positivo mayor a 0)
cantidad_input = input("Cantidad de productos: ").strip()
while not cantidad_input.isdigit() or int(cantidad_input) <= 0:
    print("Error: Ingrese un número entero mayor a 0.")
    cantidad_input = input("Cantidad de productos: ").strip()

cantidad_productos = int(cantidad_input)

# Acumuladores de totales
total_sin_descuento = 0.0
total_con_descuento = 0.0

# 3. Procesar cada producto con un ciclo for
for i in range(1, cantidad_productos + 1):
    # Validar precio (número entero positivo)
    precio_input = input(f"Producto {i} - Precio: ").strip()
    while not precio_input.isdigit() or int(precio_input) <= 0:
        print("Error: El precio debe ser un número entero mayor a 0.")
        precio_input = input(f"Producto {i} - Precio: ").strip()
    
    precio = int(precio_input)
    total_sin_descuento += precio

    # Validar opción de descuento (s/n)
    tiene_descuento = input("Descuento (S/N): ").strip().lower()
    while tiene_descuento not in ['s', 'n']:
        print("Error: Ingrese 'S' o 'N'.")
        tiene_descuento = input("Descuento (S/N): ").strip().lower()

    # Aplicar descuento del 10% si corresponde
    if tiene_descuento == 's':
        precio_final = precio * 0.90
    else:
        precio_final = float(precio)

    total_con_descuento += precio_final

# 4. Cálculos finales
ahorro_total = total_sin_descuento - total_con_descuento
promedio_por_producto = total_con_descuento / cantidad_productos

# Muestra de resultados
print(f"Total sin descuentos: ${int(total_sin_descuento)}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")