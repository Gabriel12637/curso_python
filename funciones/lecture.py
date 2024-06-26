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


## ejemplo de lambda
print (lambda n,a:f"hola, {n} , {a} "
      print(saludo("ruth","castillo")))
  

# crear un programa anonimo que reciba como parametro 
# una lista de 5 minutos y retorne dos listas uno con los 
# numeros pares y otra con numeros impares 


# Definir la función anónima
anonimo = lambda lista: ([x for x in lista if x % 2 == 0], [x for x in lista if x % 2 != 0])

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pares, impares = anonimo(lista_numeros)

print("Lista de números pares:", pares)
print("Lista de números impares:", impares)



lista_numeros =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares=lambda l:{n for n in "lista" if n%2==0}
impares=lambda l:{n for n in "lista" if n%2==0}
print(pares("lista"))
print(impares("lista"))



def mensaje(m)
    print(m)
def pedir_nombre():
    nombre=input("ingrese tu nombre")
    return nombre
mensaje(pedir_nombre())      

# map
lista=[4,7,8,5,2]
map(lambda x:x+1,lista) # por defeceto retorna una lista
nueva_lista=list(map(lambda x:x+1,lista)) #por defecto retorna una lista
print(nueva_lista)
# tengo una lista de alumnos que todos ellos aprobaron y pasan al tercer cemestre,
# problema en mi lista todos estan con el segundo
# semestre por lo que tendremos que crear una solucion que cambie el campo de semestre de 2 a 3

(
    "nombre":"abel",
    "edad":36,
    "semestre":2

),
(
    "nombre":"anthony",
    "edad":40,
    "semestre":2
),
(
    "nombre":"edith"
    "edad":50,
    "semestre":2
)
def objeto(e):
    if"semestre" in e:
        e["semestre"]=e["semestre"]+1
    return[
        e
    ]

alumnos_actualizados=list(map(objeto,lista_alumnos))
print(alumnos_actualizados)

 

# Lista de alumnos con información extendida
alumnos = [
    {"nombre": "abel", "edad": 36, "semestre": 2, "programa_estudio": "arquitectura de plataforma"},
    {"nombre": "anthony", "edad": 40, "semestre": 2, "programa_estudio": "arquitectura de plataforma"},
    {"nombre": "edith", "edad": 50, "semestre": 2, "programa_estudio": "arquitectura de plataforma"}
]

# Definimos una función para actualizar cada alumno
def actualizar_alumno(alumno):
    alumno["semestre"] = 3
    alumno["programa_estudio"] = "Arquitectura de Plataforma"
    return alumno

# Usamos map para aplicar la función a cada alumno en la lista
alumnos_actualizados = list(map(actualizar_alumno, alumnos))

# Mostrar la lista actualizada de alumnos con programa de estudio
for alumno in alumnos_actualizados:
    print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Semestre: {alumno['semestre']}, Programa de Estudio: {alumno['programa_estudio']}")



#filter
#devolver los numeros pares de una lista
lista=[4,8,2,5,7,10,6,5,2,20]
nueva_lista=list(filter(lambda x:x%2==0,lista))
print(nueva_lista)

(
    "nombre":"abel",
    "edad":36,
    "semestre":2

),
(
    "nombre":"anthony",
    "edad":40,
    "semestre":2
),
(
    "nombre":"edith"
    "edad":50,
    "semestre":2
)

lista_filtrada=(list(filter)(lambda x:x["edad"]<50,lista_alumnos))
print(lista_filtrada)











































