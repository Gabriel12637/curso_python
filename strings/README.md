 Leer los tres números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Calcular el promedio
promedio = (num1 + num2 + num3) / 3

# Imprimir el resultado
print("El promedio de los tres números es:", promedio)

2 Leer los dos números
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Comparar los números
if num1 > num2:
    print("El primer número es mayor que el segundo.")
elif num1 == num2:
    print("Ambos números son iguales.")
else:
    print("El segundo número es mayor que el primero.")

   3 # Leer el número a verificar
numero = int(input("Ingrese un número: "))

# Validar si el número está en el rango de 1 a 100
if numero >= 1 and numero <= 100:
    print("El número está en el rango de 1 a 100.")
else:
    print("El número está fuera del rango de 1 a 100.")


    4
Algoritmo CalcularVolumenEsfera
    Leer el valor del radio de la esfera
    
    Si el radio es mayor o igual a cero
        Volumen <- (4/3) * pi * radio^3
        Mostrar "El volumen de la esfera es:", Volumen
    Sino
        Mostrar "El radio debe ser mayor o igual a cero"
Fin Algoritmo
5
def calcular_area_triangulo(base, altura):
    if base > 0 and altura > 0:
        area = (base * altura) / 2
        print("El área del triángulo es:", area)
    else:
        print("Los valores de base y altura deben ser mayores que cero")

# Solicitar al usuario el valor de la base y la altura del triángulo
base = float(input("Ingrese el valor de la base del triángulo: "))
altura = float(input("Ingrese el valor de la altura del triángulo: "))

# Calcular el área del triángulo y mostrar el resultado
calcular_area_triangulo(base, altura)
6
Algoritmo ViajeAlSol
    Constante Velocidad_Luz <- 299792458 (velocidad de la luz en metros por segundo)
    Constante Distancia_Tierra_Sol <- 149.6 * 10^6 (distancia promedio entre la Tierra y el sol en kilómetros)
    
    Tiempo_Ida <- Distancia_Tierra_Sol / Velocidad_Luz
    Tiempo_Regreso <- Distancia_Tierra_Sol / Velocidad_Luz
    Tiempo_Total <- Tiempo_Ida + Tiempo_Regreso
    
    Mostrar "Tiempo estimado de viaje de ida:", Tiempo_Ida, "segundos"
    Mostrar "Tiempo estimado de viaje de regreso:", Tiempo_Regreso, "segundos"
    Mostrar "Tiempo total estimado de viaje:", Tiempo_Total, "segundos"
Fin Algoritmo
7
import math

def validar_numero_primo(n):
    if n < 2:
        print("El número no es primo")
    elif n == 2:
        print("El número es primo")
    else:
        divisores = 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                divisores += 1
                break
        if divisores == 0:
            print("El número es primo")
        else:
            print("El número no es primo")

# Solicitar al usuario un número entero
numero = int(input("Ingresa un número entero: "))

# Llamar a la función para validar si el número es primo o no
validar_numero_primo(numero)

8
def comparar_numeros(a, b):
    if a == b:
        print("Los números son iguales")
    elif a == 2 * b:
        print(a, "es el doble de", b)
    elif b == 2 * a:
        print(b, "es el doble de", a)
    else:
        print("Los números son diferentes")

# Solicitar al usuario dos números
numero_a = int(input("Ingrese el primer número: "))
numero_b = int(input("Ingrese el segundo número: "))

# Llamar a la función para comparar los números
comparar_numeros(numero_a, numero_b)
9
def calcular_area_cuadrado(lado):
    if lado > 0:
        area = lado * lado
        print("El área del cuadrado es:", area)
    else:
        print("La longitud del lado debe ser mayor que cero")

# Solicitar al usuario la longitud del lado del cuadrado
lado = float(input("Ingrese la longitud del lado del cuadrado: "))

# Calcular el área del cuadrado y mostrar el resultado
calcular_area_cuadrado(lado)
10
def convertir_kilometros_a_millas(kilometros):
    if kilometros >= 0:
        millas = kilometros * 0.621371
        print("La cantidad de millas es:", millas)
    else:
        print("La cantidad de kilómetros debe ser mayor o igual a cero")

# Solicitar al usuario la cantidad de kilómetros a convertir
kilometros = float(input("Ingrese la cantidad de kilómetros: "))

# Convertir los kilómetros a millas y mostrar el resultado
convertir_kilometros_a_millas(kilometros)
11
def dibujar_triangulo(num_filas):
    if num_filas > 0:
        for fila in range(1, num_filas + 1):
            print("*" * fila)
    else:
        print("El número de filas debe ser mayor que cero")

# Solicitar al usuario el número de filas para el triángulo
numero_filas = int(input("Ingrese el número de filas para el triángulo: "))

# Dibujar el triángulo
dibujar_triangulo(numero_filas)