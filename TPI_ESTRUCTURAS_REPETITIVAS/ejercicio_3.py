# Variables para los turnos del Lunes (4 cupos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Variables para los turnos del Martes (3 cupos)
martes1 = ""
martes2 = ""
martes3 = ""

# 1. Pedir nombre del operador (solo letras y no vacío)
operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: El nombre debe contener solo letras.")
    operador = input("Nombre del operador: ").strip()

print(f"\n¡Bienvenido/a {operador} al sistema de turnos!")

# 2. Menú principal repetitivo
opcion = ""
while opcion != "5":
    print("\n--- AGENDA DE TURNOS ---")
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    
    opcion_ingresada = input("Opción: ").strip()
    while not opcion_ingresada.isdigit() or not (1 <= int(opcion_ingresada) <= 5):
        print("Error: Ingrese una opción válida (1-5).")
        opcion_input = input("Opción: ").strip()
    
    opcion = opcion_ingresada

    # OPCIÓN 1: RESERVAR TURNO
    if opcion == "1":
        dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()
        while dia not in ["1", "2"]:
            print("Error: Seleccione 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()

        paciente = input("Nombre del paciente: ").strip()
        while not paciente.isalpha():
            print("Error: El nombre del paciente debe contener solo letras.")
            paciente = input("Nombre del paciente: ").strip()

        if dia == "1":  # LUNES
            # Verificar si ya está repetido
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print(f"Error: El paciente '{paciente}' ya tiene un turno reservado para el Lunes.")
            # Buscar primer lugar libre
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno 1 del Lunes asignado a {paciente}.")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"Turno 2 del Lunes asignado a {paciente}.")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"Turno 3 del Lunes asignado a {paciente}.")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"Turno 4 del Lunes asignado a {paciente}.")
            else:
                print("Error: No hay turnos disponibles para el Lunes.")

        else:  # MARTES
            # Verificar si ya está repetido
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print(f"Error: El paciente '{paciente}' ya tiene un turno reservado para el Martes.")
            # Buscar primer lugar libre
            elif martes1 == "":
                martes1 = paciente
                print(f"Turno 1 del Martes asignado a {paciente}.")
            elif martes2 == "":
                martes2 = paciente
                print(f"Turno 2 del Martes asignado a {paciente}.")
            elif martes3 == "":
                martes3 = paciente
                print(f"Turno 3 del Martes asignado a {paciente}.")
            else:
                print("Error: No hay turnos disponibles para el Martes.")

    # OPCIÓN 2: CANCELAR TURNO
    elif opcion == "2":
        dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()
        while dia not in ["1", "2"]:
            print("Error: Seleccione 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()

        paciente = input("Nombre del paciente a cancelar: ").strip()
        while not paciente.isalpha():
            print("Error: El nombre debe contener solo letras.")
            paciente = input("Nombre del paciente a cancelar: ").strip()

        cancelado = False

        if dia == "1":  # LUNES
            if lunes1 == paciente:
                lunes1 = ""
                cancelado = True
            elif lunes2 == paciente:
                lunes2 = ""
                cancelado = True
            elif lunes3 == paciente:
                lunes3 = ""
                cancelado = True
            elif lunes4 == paciente:
                lunes4 = ""
                cancelado = True

        else:  # MARTES
            if martes1 == paciente:
                martes1 = ""
                cancelado = True
            elif martes2 == paciente:
                martes2 = ""
                cancelado = True
            elif martes3 == paciente:
                martes3 = ""
                cancelado = True

        if cancelado:
            print(f"Turno de '{paciente}' cancelado con éxito.")
        else:
            print(f"Error: No se encontró a '{paciente}' en ese día.")

    # OPCIÓN 3: VER AGENDA DEL DÍA
    elif opcion == "3":
        dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()
        while dia not in ["1", "2"]:
            print("Error: Seleccione 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1=Lunes, 2=Martes): ").strip()

        if dia == "1":
            print("\n--- Agenda Lunes ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n--- Agenda Martes ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    # OPCIÓN 4: RESUMEN GENERAL
    elif opcion == "4":
        # Contar ocupados Lunes
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        libres_lunes = 4 - ocupados_lunes

        # Contar ocupados Martes
        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        libres_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes  -> Ocupados: {ocupados_lunes} | Disponibles: {libres_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes} | Disponibles: {libres_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Día con más turnos ocupados: Empate entre Lunes y Martes")

    # OPCIÓN 5: SALIR
    elif opcion == "5":
        print(f"\nSistema cerrado por el operador {operador}. ¡Hasta luego!")