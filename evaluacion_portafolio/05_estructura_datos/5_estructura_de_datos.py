# https://github.com/RominaOsorio/M4_evaluacion-de-portafolio

agenda = []


def mostrar_contactos():
    """Muestra todos los contactos en la agenda como diccionarios."""
    if not agenda:
        print("\n La agenda está vacía.")
        return
    print("\n--- Contactos en la agenda ---")
    for idx, contacto in enumerate(agenda, start=1):
        print(f"{idx}. {contacto}")


def buscar_contacto(nombre):
    """Busca un contacto por nombre y muestra el diccionario completo."""
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre.lower():
            print(f"\n Contacto encontrado: {contacto}")
            return
    print(f"\nNo se encontró el contacto con nombre '{nombre}'.")


def agregar_contacto():
    """Agrega un nuevo contacto con validaciones."""
    while True:
        nombre = input("Ingrese el nombre del contacto: ")
        if nombre.isalpha():
            break
        print("El nombre solo debe contener letras.")

    while True:
        apellido = input("Ingrese el apellido del contacto: ")
        if apellido.isalpha():
            break
        print("El apellido solo debe contener letras.")

    while True:
        telefono = input("Ingrese el teléfono (solo números): ")
        if telefono.isdigit() and int(telefono) > 0:
            telefono = int(telefono)
            break
        print("El teléfono debe ser un número entero positivo.")

    email = input("Ingrese el email: ")

    contacto = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
    }
    agenda.append(contacto)
    print(f"\nContacto agregado correctamente: {contacto}")


def menu():
    """Muestra el menú de opciones de la agenda."""
    while True:
        print("\n=== Agenda de Contactos ===")
        print("1. Agregar contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto por nombre")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
            if not agenda:
                print("\nLa agenda está vacía. No hay contactos para buscar.")
            else:
                nombre_busqueda = input("Ingrese el nombre del contacto a buscar: ")
                buscar_contacto(nombre_busqueda)
        elif opcion == "4":
            print("\n¡Hasta luego!\n")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
