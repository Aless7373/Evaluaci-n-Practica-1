def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Registrar nuevo estudiante")
    print("2. Agregar calificación a un estudiante")
    print("3. Mostrar información de un estudiante")
    print("4. Mostrar todos los estudiantes")
    print("5. Salir del programa")

def validar_entero_positivo(valor):
    while True:
        try:
            num = int(valor)
            if num > 0:
                return num
            else:
                raise ValueError
        except ValueError:
            valor = input("Por favor ingresa un número entero positivo: ")

def buscar_estudiante(nombre, lista_estudiantes):
    for estudiante in lista_estudiantes:
        if estudiante.nombre.lower() == nombre.lower():
            return estudiante
    return None
