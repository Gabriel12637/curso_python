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


    
    








