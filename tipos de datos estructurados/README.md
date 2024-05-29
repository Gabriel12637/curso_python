# tipos de datos estructurados (TDA - tipos de datos abstractos)
# lista - sus valores o elementos se peden actualizar.
eliminar
[ lista=["abel",20,5,2,5,false,["texto",.2]]
# tupla - sus valores o elementos no pueden ser modificados o eliminados
tupla=("abel",20,5,2,false,[])

#diccionarios
direcciones={"nombre":"antoni","edad":15,"sexo":false}

- [!TPI]
**ODSERVACION:** que los tipos de datos estructurados pueden almacenar
en su interior otros tipos de datos estructurados



## metodos
### 1. convertir texto a lista
```python
texto="hola"
list(texto)
#{"h","o","i","a"}

#metodo splint
texto="hola como estan gargolas"
texto.splin(",")
```
### 2. agregar elementos al final de una lista
``` python
# metodo append - es el metodo que me permite egregar elementos al final
de una lista
lista=["hola"]
lista.append("mundo")
print(lista)
#["hola","mundo"]

#metodo insert - es el metodo que me permite agregar elementos en cualquier ubicacion de mi lista
lista_monbres=["edith","ruth","luz"]
lista_nombres.insert(o,"antony")


### 3. eliminar elementos de una lista 
```python
# metodo pop es el que elimina el ultimo elemento de una lista
es el contrario de append .
lista_monbres=["edith","ruth","luz"]
lista_nombres.pop()

# primera manera - metodo remove - este metodo elimina el por el 
nombre el elmento que coincida dentro de la lista 
lista_monbres=["edith","ruth","luz"]
lista_nombres.remove(o,"ruth")

# segunda opcion - metodo pop_al pasarle por pametro un indice este lo eliminar de la lista
lista_monbres=["edith","ruth","luz"]
lista_nombres.pop(0)

### 4. buscar un elemento en una lista
```python
lista_monbres=["edith","ruth","luz"]
indice=lista_nombres.index("ruth)
print(lista_nombres[indice])

pertenencia="edith" in lista_nombres #true false

### 5. comparacion de lista 
podemos havcer usoo de los comparadores de comparacion para comparar listas 
**ejm:**
```python

compara=[1,2,3]>[1,2,3]
# 1 no por que son iguales en ambas listas
# 2 no por que son iguales en ambas listas
# 3 evalua que es menor que 4
# entonces la primera lista es menor que la segunda lista
print(compara)
# salida
```

### 6. cuidado con las copias

### 7. fe de errats(actualizar listas)
```python

lista=[1,3,4,5,6]
lista[0]=2
print(lista)
#[2,3,4,5,6]
#modificando lista con diccionario
alumnos=[
    {
        "nombre":"abel",
        "edad"!15
    },
    {
        "nombre":anthony".
        "edad":29

    }
]
alumnos[0["edad"]=30
alumnos[0]={"nombre":"mafer","edad":15}
alumnos[1]{"sexo"}="por definir"
print(alumnos)
```

