### Cálculo de áreas - Python

Este programa calcula el área de diferentes figuras geométricas utilizando funciones separadas para modularizar la lógica y permitir la reutilización del código.

---

### Funcionalidades

- **Área de un Cuadrado** :Solicita al usuario el lado del cuadrado (número positivo).
- **Área de un Rectángulo**: Solicita al usuario la base y la altura (números positivos).
- **Área de un Triángulo**: Solicita al usuario la base y la altura (números positivos).
- **Área de un Círculo**: Solicita al usuario el radio (número positivo).
- **Salir**: Finaliza la ejecución del programa.

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
      cd evaluacion_portafolio
   cd 06_funciones

2. Ejecutar archivo con Python