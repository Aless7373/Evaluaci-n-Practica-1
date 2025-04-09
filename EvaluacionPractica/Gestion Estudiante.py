"""
Autores: Marcos Alessandro Lagos Rivera / Axell Antonio Castillo Tapia
Versión: 1.0
Fecha: 09/04/2025
"""
from Estudiante import Estudiante
from Funciones import mostrar_menu, validar_entero_positivo, buscar_estudiante

# Lista para almacenar objetos de tipo Estudiante
estudiantes = []

# Bucle principal del programa
while True: #
    mostrar_menu()  # Mostrar el menú al usuario
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # Registrar un nuevo estudiante
        nombre = input("Nombre del estudiante: ")
        edad = validar_entero_positivo(input("Edad: "))
        carrera = input("Carrera: ")
        estudiante = Estudiante(nombre, edad, carrera)
        estudiantes.append(estudiante)
        print("Estudiante registrado exitosamente.\n")

    elif opcion == "2":
        # Agregar una calificación a un estudiante existente
        nombre = input("Nombre del estudiante: ")
        estudiante = buscar_estudiante(nombre, estudiantes)
        if estudiante:
            try:
                nota = float(input("Ingresa la nota (0-100): "))
                estudiante.agregar_calificacion(nota)
            except ValueError:
                print("Por favor ingresa un número válido.\n")
        else:
            print("Estudiante no encontrado.\n")

    elif opcion == "3":
        # Mostrar información de un estudiante
        nombre = input("Nombre del estudiante: ")
        estudiante = buscar_estudiante(nombre, estudiantes)
        if estudiante:
            estudiante.mostrar_info()
        else:
            print("Estudiante no encontrado.\n")

    elif opcion == "4":
        # Mostrar información de todos los estudiantes

        if estudiantes:
            for est in estudiantes:
                est.mostrar_info()
                print("------------------")
        else:
            print("No hay estudiantes registrados.\n")

    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intenta de nuevo.\n")
