

usuario_correcto= "alumno"
clave_correcta="python123"

intento= 0
ingreso_concedido = False

#intento de ingreso
while intento < 3 and not ingreso_concedido:
    intento += 1
    print(f"Intento {intento}/3")
    usuario = input("usuario:")
    clave= input("clave:")

    if usuario == usuario_correcto and clave == clave_correcta:
        ingreso_concedido = True
        print("acceso concedido!")
    else :
        print("Error: credenciales inválidas.")
if ingreso_concedido == False :
    print("Cuenta bloqueada")
else:
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ DE OPCIONES ---")
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4)salir")
        opcion_ingresada = input("Opción: ")

        while not opcion_ingresada.isdigit() or not (1 <= int(opcion_ingresada) <= 4):
            if not opcion_ingresada.isdigit():
                print("Error: ingrese un número válido.")
            else:
                print("Error: opción fuera de rango.")
            opcion_ingresada = input("Opción: ")

        opcion = opcion_ingresada

        # Ejecución de la opción seleccionada
        if opcion == "1":
            print("\nEstado: Inscripto")

        elif opcion == "2":
            # Cambiar clave con validaciones
            nueva_clave = input("Nueva clave: ")
            
            # Validar longitud mínima de 6 caracteres
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")

            confirmacion = input("Confirmar nueva clave: ")

            # Validar que coincidan
            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirmar nueva clave: ")

            # Actualizar la clave
            clave_correcta = nueva_clave
            print("¡Clave actualizada con éxito!")

        elif opcion == "3":
            print("\n\"El único modo de hacer un gran trabajo es amar lo que haces.\" - Steve Jobs")

        elif opcion == "4":
            print("\n¡Hasta luego!")