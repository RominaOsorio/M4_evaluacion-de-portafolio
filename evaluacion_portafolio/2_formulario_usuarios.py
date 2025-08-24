# https://github.com/RominaOsorio/M4_evaluacion-de-portafolio

while True:
    nombre = input("\nIngrese su nombre: ")
    if nombre.isalpha():
        break
    print("El nombre solo debe contener letras.")

while True:
    apellido = input("Ingrese su apellido: ")
    if apellido.isalpha():
        break
    print("El apellido solo debe contener letras.")

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break
    except ValueError:
        print("La edad debe ser un número entero.")

while True:
    try:
        estatura = float(input("Ingrese su estatura en metros: "))
        break
    except ValueError:
        print("Ingrese un número válido para la estatura.")

while True:
    respuesta = input("¿Es estudiante? (si/no): ").lower()
    if respuesta in ["si", "no"]:
        es_estudiante = True if respuesta == "si" else False
        break
    print("Escriba 'si' o 'no'.")


print("\n--- Resumen del formulario ---")
print(f"Nombre completo: {nombre} {apellido}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura} m")
print(f"¿Es estudiante?: {es_estudiante}\n")
