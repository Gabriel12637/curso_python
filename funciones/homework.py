## crear una funcion que reciba por argumentos n numeros
## y retorne una lista con numeros pares 
def num_pares(*args):
   lista_pares=[]
   for n in args:
      if n%2==0:
         lista_pares.append(n)
   return lista_pares
#por comprension
    #return [for n in args: if n%2==0:]
print(num_pares(8,5,4,7,9,25,4,7,12))
 
#crear tres funciones para los siguientes casos
#calcular el numero mayor
#calcular el numero mayor 
#calcular la suma de todos los numeros
#se le pasara por argumento n numeros
def min(*args):
    menor=args[0]
    for n in args:
        if n<menor:
            menor=n
    return menor
def max(*args):
    mayor=args[0]
    for n in args:
        if n>mayor:
            mayor=n
    return mayor
def sum(*args):


#empaqueta y desempaqueta de argumento nominal 
def  alumnos(**kwargs):
    print(kwargs)
alumnos(nombre="miguel",apellido="largo",edad=30) 


    
#crear una lista de alumnos con los siguientes campos
#nombre,apellido,edad,celular,email
#1 .actualizar los registro con un campo mas tods tendran el campo de programa de enfermeria
#2 .buscar el segundo registro y actualizar su edad a 50 años

# Crear la lista de alumnos con los campos iniciales
alumnos = [
    {"nombre": "Juan", "apellido": "Perez", "edad": 25, "celular": "123456789", "email": "juan@example.com"},
    {"nombre": "Maria", "apellido": "Gomez", "edad": 30, "celular": "987654321", "email": "maria@example.com"},
    {"nombre": "Carlos", "apellido": "Lopez", "edad": 28, "celular": "456789123", "email": "carlos@example.com"}
]

# Agregar el campo "programa" a todos los registros
for alumno in alumnos:
    alumno["programa"] = "Enfermería"

# Actualizar la edad del segundo registro a 50 años
alumnos[1]["edad"] = 50

# Mostrar la lista de alumnos actualizada
print(alumnos)







