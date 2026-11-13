

# 1. Pedir nombre del agente (solo letras y no vacío)
agente = input("agente: ")
while not agente.isalpha():
    print("error: el nombre debe contener solo letras ")
    agente = input("agente: ")



#inilizar estadisticas


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

#regla antispam
forzar_seguidos = 0



#bucle miesntras se juegue

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n--- ESTADO DEL AGENTE {agente.upper()} ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {'ACTIVADA ' if alarma else 'Desactivada'} | Código parcial: '{codigo_parcial}'")

    #menu principal
    
    print("\nMenú de acciones:")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    #validacion menu principal

    opcion_entrada = input("opcion: ")
    while not opcion_entrada.isdigit() or not (1 <= int(opcion_entrada) <= 3) :
        print("ingrese un numero entre el 1 y el 3")
        opcion_entrada = input("opcion: ")

    opcion = int(opcion_entrada)


    #OPCIÓN 1: FORZAR CERRADURA

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidos += 1
        print("intentas forzar la cerradura")

        if forzar_seguidos == 3:
            alarma = True
            print("Forzaste la cerradura 3 veces seguidas y se trabó el sistema. ¡Alarma activada!")

        else:
            #riesgo de alarma

            if energia < 40 and not alarma:
                print("Tu energía es baja (< 40). Hay riesgo de activar la alarma.")

                numero_entrada = input("Elija un número del 1 al 3: ")
                while not numero_entrada.isdigit() or not (1 <= (int(numero_entrada)) <= 3):  #VALIDACION NUMERO DE ENTRADA
                    print("Error: Debe ingresar un número entero entre 1 y 3.")
                    numero_entrada = input("Elija un número del 1 al 3: ")
                
                if int(numero_entrada) == 3:
                    alarma = True
                    print("¡Ocurrió un fallo técnico y saltó la alarma!")

            #abrir cerradura
            
            if not alarma or forzar_seguidos < 3:
                if not (forzar_seguidos == 3):
                    cerraduras_abiertas += 1
                    print(f"¡Éxito! Abriste la cerradura {cerraduras_abiertas}.")
            


    # OPCIÓN 2: HACKEAR PANEL
    elif opcion == 2:
        forzar_seguidos = 0  # Corta la racha anti-spam
        energia -= 10
        tiempo -= 3
        print("\n Hackeando panel")


        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Procesando paso {paso}/4... Código parcial actual: '{codigo_parcial}'")

        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Abriste una cerradura")
            else:
                print("abriste todas las cerraduras")

    #OPCION 3: DESCANSAR

    elif opcion == 3:
        tiempo -= 1
        forzar_seguidos = 0

        energia_recuperada = 15
        if alarma:
            print("\n Descansando (-1 tiempo)... ¡Atención! La alarma encendida genera estrés (-10 energía extra).")
            energia_recuperada -= 10
        
            energia += energia_recuperada
            if energia > 100:
                energia = 100
        
            print(f" Recuperaste energía. Energía actual: {energia}")
        
# 4. Evaluación de condiciones de fin de juego
print("\n========================================")
if cerraduras_abiertas == 3:
            print(" ¡VICTORIA! Lograste abrir las 3 cerraduras de la bóveda. Misión cumplida.")
elif alarma and tiempo <= 3:
            print(" DERROTA (Bloqueo): La alarma estaba activa y el tiempo cayó a 3 o menos. La bóveda se bloqueó por completo.")
elif energia <= 0:
            print(" DERROTA: Te quedaste sin energía.")
elif tiempo <= 0:
            print(" DERROTA: Se te agotó el tiempo.")
print("========================================")