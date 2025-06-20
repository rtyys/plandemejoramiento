# Diccionario para almacenar los datos de los estudiantes
formulario = {}

# Registrar estudiante
def Registrar_estudiante(id: int, nombre: str, edad: int, nota: float):
    # El ID es la tarjeta de identidad del estudiante
    formulario[id] = {
        "nombre": nombre,
        "edad": edad,
        "nota": nota
    }
    print(f"Estudiante {id} registrado correctamente.")
    return

# Consultar estudiante por ID
def consultar_estudiante(id: int):
    if id in formulario:
        estudiante = formulario[id]
        print(f"ID: {id}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Nota: {estudiante['nota']}")
    else:
        print("El estudiante no se encuentra registrado.")
    return

# Actualizar nota de un estudiante
def actualizar_de_notas(id: int, nueva_nota: float):
    if id in formulario:
        formulario[id]["nota"] = nueva_nota
        print(f"Nota del estudiante {id} actualizada correctamente.")
    else:
        print("El estudiante no se encuentra registrado.")
    return

# Eliminar estudiante
def eliminar_estudiante(id: int):
    if id in formulario:
        del formulario[id]
        print(f"Estudiante {id} eliminado correctamente.")
    else:
        print("El estudiante no se encuentra registrado.")
    return

# Ver todos los estudiantes registrados
def ver_todos_los_estudiantes():
    if not formulario:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes:")
        for id, estudiante in formulario.items():
            print(f"ID: {id}, Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Nota: {estudiante['nota']:.2f}")
    return

# Menú interactivo
while True:
    print("\n*** Menú Académico ***")
    print("1. Registrar Estudiante")
    print("2. Consultar Estudiante")
    print("3. Actualizar Notas")
    print("4. Eliminar Estudiante")
    print("5. Ver Todos los Estudiantes")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = int(input("Ingrese el ID del estudiante: "))
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        nota = float(input("Ingrese la nota del estudiante: "))
        Registrar_estudiante(id, nombre, edad, nota)

    elif opcion == "2":
        id = int(input("Ingrese el ID del estudiante a consultar: "))
        consultar_estudiante(id)

    elif opcion == "3":
        id = int(input("Ingrese el ID del estudiante a actualizar la nota: "))
        nueva_nota = float(input("Ingrese la nueva nota: "))
        actualizar_de_notas(id, nueva_nota)

    elif opcion == "4":
        id = int(input("Ingrese el ID del estudiante a eliminar: "))
        eliminar_estudiante(id)

    elif opcion == "5":
        ver_todos_los_estudiantes()

    elif opcion == "6":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, intente de nuevo.")
