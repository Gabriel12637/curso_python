# funciones 
## concepto
matematicamente es una funcion es una operacion 
que toma uno o mas valores llamados
*argumentos* y produce un valor denominado
*resultado*
> [!nota]
> todos los lenguajes de programacion tiene
funciones incorporadas (*funciones internas*)
, y funciones creadas por el usuario (*funciones externas*)
en programacion es una funcion es un subprograma, es una 
estructura que nos permite agrupar codigo y sus principales 
objetivos son :
- *no permitir* fracmentos de codigo
- *reutilizar* el codigo en distintos escenarios 
## estructura de funcion
una funcion tiene *definida* por un *nombre* , sus *parametros* 
y su valor *retorno* una ves creado la funcion podremos solicitar
su ejecucion *invocando* la funcion *nombre*  
## definir una funcion de python  
para definir una funcion en python usaremos la palabra 
reservada *def* seguida por el *nombre* de la funcion.
a continuacion especicaremos los *parametros*
con *()* si es una funcion sin parametros, *(a)* si es una 
funcion con parametros, si se tuviera mas de un parametros 
iran separados *,* finalizaremos la linea con *;* , en la siguiente 
linea sin olvidar el identado) que puede contener 1 o mas sentencias,
finalmente  devere *retornar* un resultado con la palabra reservada *return*
>[!info]
> como retorno tambien se puede utilizar *funcion interna*,*print()*
,para depuracion de codigo no es recomendable usarlo en produccion.
print dentro de una funcion es una herramienta que nos permite comprobar si una funcion esta haciendo su tarea correctamente 

**ejemplo** 
```python 
def saludo():
    saludo="hola chivo"
    saludo_dos="como estas"
    return f"{saludo},{saludo_dos}"
    #printf"{saludo},{saludo_dos}"
print(saludo())
```

## invocar una funcion 
para invocar una funcion , (o llamar ,ejecutar) una funcion solo tendremos que 
escribir el *nombre* de la funcion seguido por *()* parentesis 
```python
def saludo():
    print("hola")
#invocando la funcion
saludo()
```

## retornar un valor 
las funciones pueden retornar (o devolver) un valor 
```python
def uno():
    return
uno()
```
>[!WARNING]
>no confundir *print*con*return*, el valor retornado por 
*return* nos permite usalo fuera de su contexto. y *print()*
solo mostrara el literal por terminal.
**ejemplo** 
en el archivo  *lecture.py*
## retornando multiples valores 
el secreto es hacerlo mediante un tipo de dato estructurado
```python 
def valor():
    return 2,3,4
varios()
#retorna (2,3,4)
def lista():
    return["hola",45]
#retorna"hola",45] 
def dicc():
    return {"nombre":"jose","edad": 45}
dicc()
#return {"nombre":"jose","edad": 45}
```
## parametros y argumentos 
si una funcion no dispusiera de valores de entrada estaria limitada en su actuacion.
es por ello  que los *parametros* no permiten variar los datos que consume una funcion 
para obtener distintos resultados 
**ejemplo**
*crear una funcion que recibe un valor numerico y retorna una raiz cuadrada*
```python 
def sqrt(valor):
    return valor**(1/2)
# NOTA: en este caso el valor 4 es un argumento de la funcion 
sqrt(4)
```
cuando llamamos auna funcion con *argumentos*, los valores de estos argumentos se 
copian en los correspondiente *parametros* dentro de la funcion.
```python 
def ejem(a,b,c):
    return a+b+c
ejm(a,b,c)
```
### argumentos nominales 
en esta aproximacion los argumentos no son copiados en un orden especifico sino que 
**se asignan por un nombre a cada parametro** , ello nos permite evitar el problema 
de conocer o recordar cual es el orden de los parametro de la definicion de la funcion
para utilizarlo, basta con realizar una asignacion de cada argumento en la propia
llamada de funsion 
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
        """)
# haciendo uso de argumentos nominales 
buill_cpu(num_core=4,familia="intel",frecuencia=2.7)
```
### argumentos posicionales
los argumentos son copiados en un orden especifico, en este caso debemos conocer o
recordar cual es orden de los parametros
**ejemplo**
```python
def build_cpu(familia,num_core,frecuencia):
    print(f"""
        la cpu es de la familia {familia},
        con {num_core} cores y con una
        frecuencia de {frecuencia}
        """)
# haciendo uso de argumentos posicionales 
buill_cpu("intel"4,2,7)
```
### parametros por defecto
es posible especificar **valor por defecto** en los parametros 
en una funsion en el caso que no se proporcione un valor 
al argumento en la llamada ejecucion el parametro correspondiente 
tomara el valor definido por el defecto.
**ejemplo**
```python
def alumnos(nom,app,estados="aprobado"):

alumno("ruth","castillo")
alumno("anthony","crucez","desaprobado")
```








### desempaquetado/empaquetado de argumentos(tarea)
El empaquetado y desempaquetado de argumentos en Python es una característica poderosa que te permite trabajar con un número variable de argumentos en una función. Aquí te explico ambos conceptos:

### Empaquetado de Argumentos:
El empaquetado de argumentos te permite pasar un número variable de argumentos a una función. Puedes empaquetar los argumentos utilizando el operador `*` (para tuplas) o `**` (para diccionarios).

#### Empaquetado de argumentos posicionales (tuplas):
```python
def mi_funcion(*args):
    for arg in args:
        print(arg)

mi_funcion(1, 2, 3)  # Empaquetando los argumentos 1, 2 y 3 en una tupla args
```

#### Empaquetado de argumentos de palabra clave (diccionarios):
```python
def mi_funcion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mi_funcion(nombre="Juan", edad=30)  # Empaquetando los argumentos en un diccionario kwargs
```

### Desempaquetado de Argumentos:
El desempaquetado de argumentos te permite pasar una secuencia de argumentos a una función ya empaquetados. Esto se hace utilizando los mismos operadores `*` y `**`.

#### Desempaquetado de argumentos posicionales (tuplas):
```python
def mi_funcion(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
mi_funcion(*args)  # Desempaquetando los argumentos de la tupla y pasándolos a la función
```

#### Desempaquetado de argumentos de palabra clave (diccionarios):
```python
def mi_funcion(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")

kwargs = {"nombre": "Juan", "edad": 30}
mi_funcion(**kwargs)  # Desempaquetando los argumentos del diccionario y pasándolos a la función
```

El empaquetado y desempaquetado de argumentos son especialmente útiles cuando trabajas con funciones que pueden aceptar un número variable de argumentos, ya sea en forma de tuplas o diccionarios.




## funciones internas de python (tarea)
 1.print(): Para imprimir mensajes en la consola
```python
mensaje = "Hola, mundo!"
print(mensaje)
```
2.len(): Para obtener la longitud de un objeto iterable (como una lista o una cadena)
```python
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
print("La longitud de la lista es:", longitud)
```
3.input(): Para recibir la entrada del usuario desde la consola.
```python
nombre = input("Por favor, ingresa tu nombre: ")
print("Hola,", nombre)
```
4.type(): Para obtener el tipo de un objeto.
```python
numero = 42
tipo = type(numero)
print("El tipo de 'numero' es:", tipo)
```
5.range(): Para generar una secuencia de números
```python
numeros = range(5)
print(list(numeros))  # Convertimos el rango a una lista para imprimirlo
```
6.open(): Para abrir archivos en modo de lectura, escritura o ambos
```python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
```
7.sum(): Para sumar los elementos de un iterable
```python
numeros = [1, 2, 3, 4, 5]
total = sum(numeros)
print("La suma de los números es:", total)
```
8.min() y max(): Para obtener el mínimo y el máximo de un iterable.
```python
numeros = [10, 5, 8, 20, 3]
minimo = min(numeros)
maximo = max(numeros)
print("El mínimo es:", minimo)
print("El máximo es:", maximo)
```
9.abs(): Para obtener el valor absoluto de un número
```python
numero = -42
absoluto = abs(numero)
print("El valor absoluto de", numero, "es:", absoluto)
```
10.str(), int(), float(), list(), tuple(), dict(), set(): Para convertir entre diferentes tipos de datos
```python
cadena = "123"
numero = int(cadena)
print("El número es:", numero)
```