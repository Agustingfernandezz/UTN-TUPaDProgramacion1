

#nombre de usuario y validacion

print("--- BIENVENIDO A LA ARENA ---")

nombre_gladiador = input("Nombre del gladiador: ")
while not nombre_gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    nombre_gladiador = input("ingrese su usuario: ")


#INCIALIZAR VARIABLES

Vida_del_Gladiador = 100 
Pociones_de_Vida = 3 
Daño_base_Ataque_Pesado = 15
Turno_Gladiador = True 


Daño_base_del_enemigo = 12 
Vida_del_Enemigo = 100 


#BUCLE DEL JUEGO


#PANEL DE INFORMACION
while Vida_del_Gladiador > 0 and Vida_del_Enemigo > 0:
    print("\n=== INICIO DEL COMBATE === ")
    print(f"\n{nombre_gladiador} (HP:{Vida_del_Gladiador}) | Enemigo (HP:{Vida_del_Enemigo}) | Pociones: {Pociones_de_Vida}")


    #MENU DE OPCIONES
        
    print("Elige una opcion: ")
    print("1. Ataque pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar ")


        #VALIDACION ENTRADA NUMERICA


    opcion_entrada = input("Elige accion: ")

    while  not opcion_entrada.isdigit() or not 1 <=(int(opcion_entrada) <= 3):
        print("Error: Ingrese un número válido.")
        opcion_entrada = input("Elige accion: ")
    opcion = int(opcion_entrada)


        #OPCION 1: ATAQUE PESADO


    if  opcion == 1:

        if Vida_del_Enemigo > 20:        
            print(f"¡Atacaste al enemigo por {Daño_base_Ataque_Pesado} puntos de daño!")
            Vida_del_Enemigo -= Daño_base_Ataque_Pesado


        elif Vida_del_Enemigo <= 20 and Vida_del_Enemigo > 0:            
            print("Golpe critico!")
            print(f"¡Atacaste al enemigo por {Daño_base_Ataque_Pesado * 1.5} puntos de daño!")
            Vida_del_Enemigo -= float(Daño_base_Ataque_Pesado * 1.5)

        else:
            pass

        #OPCION 2: RAFAGA VELOZ

    elif opcion == 2:
        print(">>¡Inicias una ráfaga de golpes!")

        for golpe in range(1,4):
            Vida_del_Enemigo -= 5
            print(">Golpe conectado por 5 de daño")

        #OPCION 3: CURAR

    elif opcion == 3:

        if Pociones_de_Vida >0:
            Vida_del_Gladiador += 30
            Pociones_de_Vida -= 1
            print(f" Te has curado 30 puntos de vida. Te quedan {Pociones_de_Vida} pociones.")

        else:
            print("¡No quedan pociones!")

    #ATAQUE ENEMIGO

    if Vida_del_Enemigo > 0:
        Vida_del_Gladiador -= Daño_base_del_enemigo
        print(f"\n¡El enemigo te atacó por {Daño_base_del_enemigo} puntos de daño!")



#EVALUACION FINAL DEL JUEGO


print("\n===========================================")
if Vida_del_Gladiador > 0:
    print(f" ¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
else:
    print(" DERROTA. Has caído en combate.")
print("===========================================")
