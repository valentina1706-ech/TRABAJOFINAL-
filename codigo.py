# Diccionarios para almacenar usuarios y citas
# Precargando información inicial

usuarios = {
    "1012345678": {"nombre": "Juan Pérez", "contraseña": "juan123"},
    "1023456789": {"nombre": "Ana López", "contraseña": "ana456"},
    "1034567890": {"nombre": "Roberto Gómez", "contraseña": "luis789"},
    "1045678901": {"nombre": "María Torres", "contraseña": "maria321"},
}

citas = {
    "1012345678": {
        "fecha": "05/12/2024",
        "hora": "10:00",
        "tipo": "Consulta General",
        "medico": "Dr. González"
    },
    "1023456789": {
        "fecha": "10/12/2024",
        "hora": "15:30",
        "tipo": "Consulta Especialista",
        "medico": "Dra. Martínez"
    },
    "1034567890": {
        "fecha": "15/12/2024",
        "hora": "13:00",
        "tipo": "Control Prenatal",
        "medico": "Dra. Ramírez"
    },
}

#_______________________________________________________________________________________________________________-
# Usuarios y contraseñas de administradores (solo estos dos usuarios pueden ingresar al menu de administradores)
usuarios_validos = {
    "carlostorres": "4611579",
    "valentina": "123456",
}

# Funciones para los menús
# _____________________________________________________________________________________________________
#menu principal

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Consultar cita")
    print("2. Menú Administrador")
    print("3. Salir")
#__________________________________________________________________________________________________________
# menu de administrador

def mostrar_menu_administrador():
    print("\n--- Menú Administrador ---")
    print("1. Agregar usuario")
    print("2. Agregar cita")
    print("3. Confirmar o cancelar cita")
    print("4. Imprimir reporte de datos")
    print("5. Volver al menú principal")
    print("6. Salir completamente")

# Función para validar administradores
# _____________________________________________________________________________________________________
def validar_usuario():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario in usuarios_validos and usuarios_validos[usuario] == contraseña:
        print("Acceso concedido.")
        return True
    else:
        print("Usuario o contraseña incorrectos.")
        return False

# Funciones del menú administrador
# ________________________________________________________________________________________________________________
def agregar_usuario():
    print("\n--- Agregar Usuario ---")
    cedula = input("Ingrese la cédula del usuario: ")
    if cedula in usuarios:
        print("El usuario ya existe.")
    else:
        nombre = input("Ingrese el nombre del usuario: ")
        contraseña = input("Ingrese una contraseña para el usuario: ")
        usuarios[cedula] = {"nombre": nombre, "contraseña": contraseña}
        print("Usuario agregado exitosamente.")
#_______________________________________________________________________________________________________________
# funcion para agregar citas

def agregar_cita():
    print("\n--- Agregar Cita ---")
    print("Recuerda que el usario a registrar debe estar en nuestra base de datos")
    cedula = input("Ingrese la cédula del usuario: ")
    if cedula not in usuarios:
        print("El usuario no existe. Regístrelo primero.")
    else:
        fecha = input("Ingrese la fecha de la cita (DD/MM/AAAA): ")
        hora = input("Ingrese la hora de la cita (HH:MM): ")
        tipo = input("Ingrese el tipo de cita (General, Especialista, etc.): ")
        medico = input("Ingrese el nombre del médico: ")
        citas[cedula] = {
            "fecha": fecha,
            "hora": hora,
            "tipo": tipo,
            "medico": medico,
        }
        print("Cita asignada exitosamente.")
#____________________________________________________________________________________________________________________
# funcion para gestionar las citas

def gestionar_cita():
    print("\n--- Confirmar o Cancelar Cita ---")
    cedula = input("Ingrese la cédula del usuario: ")
    if cedula not in citas:
        print("No hay citas registradas para este usuario.")
    else:
        print(f"Cita actual: {citas[cedula]}")
        accion = input("¿Desea confirmar (C) o cancelar (X) la cita? ").upper()
        if accion == "C":
            print("Cita confirmada.")
        elif accion == "X":
            del citas[cedula]
            print("Cita cancelada.")
        else:
            print("Acción no válida.")
#___________________________________________________________________________________________________________________
# funcion para imprimir los reportes que tenemos o citas en su defecto, preguardadas


def imprimir_reporte():
    print("\n--- Reporte de Datos ---")
    print("Usuarios:")
    for cedula, info in usuarios.items():
        print(f"- {cedula}: {info}")
    print("\nCitas:")
    for cedula, info in citas.items():
        print(f"- {cedula}: {info}")

#____________________________________________________________________________________________________________________
# consultar cita del usuario, este acceso solo funciona si el usuario se encuentra en nuestra base de datos 

def consultar_cita():
    print("\n--- Consultar Cita ---")
    cedula = input("Ingrese su cédula: ")
    if cedula in citas:
        cita = citas[cedula]
        print("\nInformación de la cita:")
        print(f"- Fecha: {cita['fecha']}")
        print(f"- Hora: {cita['hora']}")
        print(f"- Tipo: {cita['tipo']}")
        print(f"- Médico: {cita['medico']}")
    else:
        print("No se encontró una cita asociada a esta cédula.")


# Menú del administrador
# ______________________________________________________________________________________________________________________
def menu_administrador():
    while True:
        mostrar_menu_administrador()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            agregar_cita()
        elif opcion == "3":
            gestionar_cita()
        elif opcion == "4":
            imprimir_reporte()
        elif opcion == "5":
            break
        elif opcion == "6":
            print("Saliendo completamente del sistema...")
            return "exit"
        else:
            print("Opción no válida. Intente de nuevo.")

# Menú principal
# ____________________________________________________________________________________________________________________
# funcion madre donde se enlazan todas las funciones creadas previamente

def menu():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            consultar_cita()
        elif opcion == "2":
            if validar_usuario():
                resultado = menu_administrador()
                if resultado == "exit":
                    break
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Llamada al menú principal
# __________________________________________________________________________________________________________________
menu()
