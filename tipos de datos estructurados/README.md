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