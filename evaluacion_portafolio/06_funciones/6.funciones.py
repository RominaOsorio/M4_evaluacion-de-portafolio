# https://github.com/RominaOsorio/M4_evaluacion-de-portafolio

import math


def area_cuadrado(lado):
    return lado**2


def area_rectangulo(base, altura):
    return base * altura


def area_triangulo(base, altura):
    return (base * altura) / 2


def area_circulo(radio):
    """Calcula el área de un círculo."""
    return math.pi * radio**2


def solicitar_numero_positivo(prompt):
    while True:
        try:
            valor = float(input(prompt))
            if valor > 0:
                return valor
            else:
                print("Debe ingresar un número positivo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número.")


def menu():
    while True:
        print("\n=== Calculadora de Áreas ===")
        print("1. Área de un cuadrado")
        print("2. Área de un rectángulo")
        print("3. Área de un triángulo")
        print("4. Área de un círculo")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            lado = solicitar_numero_positivo("Ingrese el lado del cuadrado: ")
            print(f"\nEl área del cuadrado es: {area_cuadrado(lado):.2f}\n")
        elif opcion == "2":
            base = solicitar_numero_positivo("Ingrese la base del rectángulo: ")
            altura = solicitar_numero_positivo("Ingrese la altura del rectángulo: ")
            print(f"\nEl área del rectángulo es: {area_rectangulo(base, altura):.2f}\n")
        elif opcion == "3":
            base = solicitar_numero_positivo("Ingrese la base del triángulo: ")
            altura = solicitar_numero_positivo("Ingrese la altura del triángulo: ")
            print(f"\nEl área del triángulo es: {area_triangulo(base, altura):.2f}\n")
        elif opcion == "4":
            radio = solicitar_numero_positivo("Ingrese el radio del círculo: ")
            print(f"\nEl área del círculo es: {area_circulo(radio):.2f}\n")
        elif opcion == "5":
            print("\n¡Hasta luego!\n")
            break
        else:
            print("\nOpción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
