# averiguar sobre modulos y paquetes de python
# diferencias entre modulos y paquetes

### Módulos:

Un módulo en Python es simplemente un archivo que contiene definiciones de funciones, clases y variables. Estos archivos tienen extensión `.py` y contienen código Python ejecutable.

- **Ejemplo de módulo:**
  Supongamos que tienes un archivo llamado `mimodulo.py` que contiene funciones y variables:
  
  ```python
  # mimodulo.py
  
  def saludar(nombre):
      print(f"Hola, {nombre}!")
  
  def calcular_cuadrado(numero):
      return numero ** 2
  
  pi = 3.14159
  ```

  Este archivo se convierte en un módulo que puedes importar en otros programas Python para utilizar las funciones `saludar`, `calcular_cuadrado`, y la variable `pi`.

- **Uso de un módulo:**
  Para usar las funciones y variables definidas en `mimodulo.py` en otro archivo Python, puedes importarlo de la siguiente manera:
  
  ```python
  import mimodulo
  
  mimodulo.saludar("Juan")
  print(mimodulo.pi)
  ```

### Paquetes:

Los paquetes en Python son colecciones de módulos. Esencialmente, un paquete es una carpeta que contiene varios archivos de módulos y un archivo especial llamado `__init__.py`, que puede estar vacío o puede contener código de inicialización para el paquete.

- **Ejemplo de estructura de paquete:**
  
  ```
  mi_paquete/
  │
  ├── __init__.py
  ├── modulo1.py
  └── modulo2.py
  ```

  En este ejemplo, `mi_paquete` es un paquete que contiene los módulos `modulo1.py` y `modulo2.py`, además del archivo `__init__.py`.

- **Uso de un paquete:**
  Para importar módulos desde un paquete en Python, puedes hacerlo de varias maneras:
  
  ```python
  import mi_paquete.modulo1
  from mi_paquete import modulo2
  
  mi_paquete.modulo1.funcion()
  modulo2.otra_funcion()
  ```

### Diferencias clave:

- **Módulo:** Es un archivo individual que contiene código Python.
- **Paquete:** Es una carpeta que contiene múltiples archivos de módulo y opcionalmente un archivo `__init__.py`.

En resumen, los módulos y paquetes en Python son herramientas poderosas para organizar y estructurar el código, facilitando la reutilización y la modularidad en proyectos de cualquier tamaño.