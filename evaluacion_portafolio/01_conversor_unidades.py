# # https://github.com/RominaOsorio/M4_evaluacion-de-portafolio


while True:
    print("\n=== Conversor de Unidades ===")
    print("1. Peso (gramos, kilos, toneladas)")
    print("2. Divisas (CLP, USD, EUR)")
    print("3. Tiempo (horas, minutos, segundos)")
    print("4. Salir")

    opcion_str = input("Seleccione una opción (1-4): ").strip()

    try:
        opcion = int(opcion_str)
    except ValueError:
        print("\nDebes ingresar un número entre 1 y 4.")
        continue

    if opcion not in (1, 2, 3, 4):
        print("\nDebes ingresar un número entre 1 y 4.")
        continue

    if opcion == 1:
        try:
            gramos = float(input("\nIngrese la cantidad en gramos: ").strip())
            if gramos < 0:
                print("El valor no puede ser negativo.")
                continue
        except ValueError:
            print("Ingresa un número válido para gramos.")
            continue

        kilos = gramos / 1000
        toneladas = gramos / 1_000_000

        print(f"\n{gramos} gramos equivalen a:")
        print(f"- {kilos} kilogramos")
        print(f"- {toneladas} toneladas")

    elif opcion == 2:
        print("\nTasas de cambio usadas:")
        print("1 USD = 950 CLP")
        print("1 EUR = 1050 CLP")

        try:
            pesos = float(
                input("\nIngrese la cantidad en Pesos Chilenos (CLP): ").strip()
            )
            if pesos < 0:
                print("El valor no puede ser negativo.")
                continue
        except ValueError:
            print("Ingresa un número válido para CLP.")
            continue

        usd = pesos / 950
        eur = pesos / 1050

        print(f"\n{int(pesos)} CLP equivalen a:")
        print(f"- {usd:.2f} dólares (USD)")
        print(f"- {eur:.2f} euros (EUR)")

    elif opcion == 3:
        try:
            horas = float(input("\nIngrese la cantidad en horas: ").strip())
            if horas < 0:
                print("El valor no puede ser negativo.")
                continue
        except ValueError:
            print("Ingresa un número válido para horas.")
            continue

        minutos = int(horas * 60)
        segundos = int(horas * 3600)

        print(f"\n{int(horas)} horas equivalen a:")
        print(f"- {minutos} minutos")
        print(f"- {segundos} segundos")

    elif opcion == 4:
        print("\n¡Hasta luego!\n")
        break
