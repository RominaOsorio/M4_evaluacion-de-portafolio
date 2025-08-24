## Evaluación de Portafolio - Python

Este proyecto corresponde a la evaluación final del modulo 4 del curso de Python, en el cual se aplican las competencias técnicas adquiridas a lo largo de las clases.
El objetivo es demostrar el dominio de los fundamentos del lenguaje Python mediante la implementación de programas simples, organizados en distintos archivos para mayor claridad.

---

### Tecnologías utilizadas
- Lenguaje: Python
- Control de versiones: Git y GitHub
- Entorno: Consola / Terminal

---

### `1_conversor_unidades.py`

Este programa utiliza los conceptos fundamentales del lenguaje Python para la construcción de programas.

El conversor implementa el uso de:
- **Variables** (para almacenar los valores ingresados y calculados).
- **Operadores matemáticos** (suma, división, multiplicación).
- **Estructuras condicionales** (`if`, `elif`, `else`).
- **Bucles** (`while True`) para repetir el menú hasta que el usuario decida salir.
- **Entrada y salida de datos** (`input()` y `print()`).

---

### Funcionalidades

El programa permite elegir entre tres tipos de conversores:

1. **Peso (gramos, kilos, toneladas)**
- Convierte gramos a kilogramos y toneladas.

2. **Divisas (Pesos Chilenos → USD / EUR)**
- Convierte pesos chilenos a dólares y euros usando tasas de cambio predefinidas.

3. **Tiempo (horas → minutos y segundos)**
- Convierte una cantidad de horas en minutos y segundos.

4. **Salir**
- Finaliza el programa.

---

### `2_formulario_usuarios.py`


Formulario en Consola - Tipos de Datos en Python
Este proyecto consiste en un script en Python que solicita información al usuario desde la consola, utilizando distintos tipos de datos (cadenas, enteros, flotantes y booleanos).
Además, incluye validaciones para asegurar que el usuario ingrese datos correctos según el tipo esperado.

---

### Funcionalidades

- Solicita el nombre y el apellido (validados como cadenas sin números).
- Solicita la edad, validada como número entero.
- Solicita la estatura, validada como número decimal (float).
- Pregunta si el usuario es estudiante, con respuesta de tipo booleano (True o False).
- Muestra un resumen final con todos los datos ingresados.

---

### `3-condicionales.py`

Este programa aplica el uso de estructuras de control de flujo en Python (if, elif, else) para resolver un problema simple: determinar si un número es positivo, negativo o cero.
Además, se incluye una validación de entrada que garantiza que el usuario ingrese solo valores numéricos (enteros o flotantes).

---

### Funcionalidades

- El usuario ingresa un número.
- El programa valida que efectivamente sea un número (admite tanto int como float).
- Se determina si el número ingresado es: Positivo, negativo o cero

Si el número no tiene decimales (ejemplo: 5.0), el programa lo muestra como un entero (5) para mejorar la presentación.

---

### `4_iteraciones.py`


Este programa combina dos ejercicios que utilizan sentencias iterativas (for y while) para resolver problemas simples en Python:
Generar tablas de multiplicar usando un bucle for.
Calcular el factorial de un número usando un bucle while.
Se incluyen validaciones para asegurar que el usuario ingrese datos correctos (números enteros positivos).

---

### Funcionalidades

**Tablas de Multiplicar (bucle for)**
- El usuario ingresa un número entero y un límite hasta el cual desea multiplicar.
- Se imprime la tabla de multiplicar completa desde 1 hasta el límite.
- Se utiliza un bucle for para iterar y calcular los resultados.

**Calculadora de Factoriales (bucle while)**
- El usuario ingresa un número entero mayor o igual a 0.
- El programa calcula el factorial de ese número utilizando un bucle while.

---

### `5_estructura_de_datos.py`

Este programa implementa un sistema de agenda de contactos usando listas y diccionarios en Python.
Permite almacenar, mostrar y buscar contactos con validaciones robustas, mostrando los contactos como diccionarios completos para fines pedagógicos.

---

### Funcionalidades

**Agregar Contacto**
- El usuario ingresa: nombre, apellido, teléfono y email.
- Validaciones:
  - Nombre y apellido: solo letras (`str`).
  - Teléfono: solo números enteros positivos (`int`).
- Cada contacto se almacena como un diccionario en la lista `agenda`.

**Mostrar Todos los Contactos**
- Muestra todos los contactos almacenados en la lista `agenda`.
- Si la agenda está vacía, muestra el mensaje:

---

### `6_funciones.py`

Este programa calcula el área de diferentes figuras geométricas utilizando funciones separadas para modularizar la lógica y permitir la reutilización del código.

---

### Funcionalidades

- **Área de un Cuadrado** :Solicita al usuario el lado del cuadrado (número positivo).
- **Área de un Rectángulo**: Solicita al usuario la base y la altura (números positivos).
- **Área de un Triángulo**: Solicita al usuario la base y la altura (números positivos).
- **Área de un Círculo**: Solicita al usuario el radio (número positivo).
- **Salir**: Finaliza la ejecución del programa.

---

### Validaciones y Reutilización de Código

Todas las entradas numéricas se validan con la función:

def solicitar_numero_positivo(prompt):
    ...

- Esto evita duplicar código de validación en cada opción del menú.
- Cada cálculo está separado en funciones, lo que permite modularización y reutilización.
- Fácil de extender agregando nuevas figuras con sus propias funciones.


### Cómo ejecutar los programas

1. Clonar este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/evaluacion_portafolio.git
   cd evaluacion_portafolio

2. Ejecutar los archivo con Python
