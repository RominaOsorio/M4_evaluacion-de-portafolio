# https://github.com/RominaOsorio/M4_evaluacion-de-portafolio

while True:
    numero_str = input("\nIngrese un número: ")
    try:
        numero = float(numero_str)

        if numero.is_integer():
            numero = int(numero)

        if numero > 0:
            print(f"El número {numero} es positivo.\n")
        elif numero < 0:
            print(f"El número {numero} es negativo.\n")
        else:
            print("El número es cero.\n")
        break
    except ValueError:
        print(
            "Entrada no válida. Por favor ingrese solo números (enteros o decimales)."
        )
