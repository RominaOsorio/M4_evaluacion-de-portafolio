# https://github.com/RominaOsorio/M4_evaluacion-de-portafolio

import math


while True:
    try:
        numero_tabla = int(
            input("\nIngrese un número entero para generar su tabla de multiplicar: ")
        )
        break
    except ValueError:
        print("Debe ingresar un número entero válido.")

while True:
    try:
        limite_tabla = int(input("¿Hasta qué número desea multiplicar?: "))
        if limite_tabla > 0:
            break
        else:
            print("Debe ingresar un número positivo.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

print(f"\nTabla de multiplicar del {numero_tabla} utilizando for:")
for i in range(1, limite_tabla + 1):
    print(f"{numero_tabla} x {i} = {numero_tabla * i}")


while True:
    try:
        numero_fact = int(
            input("\nIngrese un número entero para calcular su factorial: ")
        )
        if numero_fact >= 0:
            break
        else:
            print("El número debe ser mayor o igual a 0.")
    except ValueError:
        print("Debe ingresar un número entero válido.")

factorial = 1
contador = numero_fact

if numero_fact == 0:
    factorial = 1
else:
    while contador > 1:
        factorial *= contador
        contador -= 1
print(f"\nUtilizando while")
print(f"El factorial de {numero_fact} es: {factorial}\n")
