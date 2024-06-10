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