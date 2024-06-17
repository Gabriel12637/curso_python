# return devuelve valores que podre hacer uno 
# crear una funcion que retorne el numero 10 y muestre por terminal
# si es par
# siempre que el valor que retorne mi funcion se utilize en mas sentencios 
# u operaciones 
def diez():
    return 10
if diez()%2==0:
    print("es par")
else:
    print("es impar")
# print solo muestra por terminal

# return cuando queremos que nuestra funcion retorne un tipo de dato
# o un tipo de dato estructurado

# crear una funcion que muestre el producto de dos nuemeros
def producto(a,b):
    return a*b

# cear una funcion que me retorne una lista de tres numeros
def lista_numeros():
    return[3,2,6]

# print usaremos cada vez que muestre funcion retorno un mensaje

# crear una funcion que por parametro reciba un nombre y retorno un 
# mensaje de bienvenida con el nombre 
def mensaje(nombre):
    print(f"hola, (nombre), bienvenido al chongo")


# crear una funcion que reciba por parametro una lista de numeros y me devuelva 
# y se devuelva el numero menor, mostrar por terminal el valor retornado por la funcion 

def encontrar_menor(numero):
    return numero

# Ejemplo de uso
numero = 3
menor_numero = encontrar_menor(numero)
print("El número menor es:", menor_numero)


# crear una funcion que reciba como parametro el nombre y la edad de una persona la 
# funcion debere retornaar un diccion con los datos,luego motrarpor terminal el valor
# de retorno  de la funcion 

def obtener_datos_persona(nombre, edad):
    datos_persona = {"nombre": nombre, "edad": edad}
    return datos_persona

# Ejemplo de uso
nombre = input("Ingrese el nombre de la persona: ")
edad = int(input("Ingrese la edad de la persona: "))

datos = obtener_datos_persona(nombre, edad)
print("Datos de la persona:", datos)



  



























































