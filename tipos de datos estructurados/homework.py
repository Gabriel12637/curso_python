# crea una lista de circo alumnos cada alunmnos almacenaremos su nombre 
# apellido y edad 

# insertar al final de la lista los datos de antoni

# eliminar de la lista si existe los datos de abel

# buscar y mostrar el alumnos en la posicion 4 de la lista

# Creamos una lista vacía para almacenar los datos de los alumnos del circo
lista_alumnos_circo = []

# Función para insertar datos de un alumno al final de la lista
def insertar_alumno(nombre, apellido, edad):
    lista_alumnos_circo.append({"nombre": nombre, "apellido": apellido, "edad": edad})

# Función para eliminar los datos de un alumno si existe en la lista
def eliminar_alumno(nombre):
    for alumno in lista_alumnos:
        if alumno["nombre"] == nombre:
            lista_alumnos_circo.remove(alumno)
            print(f"Los datos de {nombre} han sido eliminados de la lista.")
            return
    print(f"No se encontraron datos de {nombre} en la lista.")

# Función para buscar y mostrar el alumno en una posición específica de la lista
def mostrar_alumno_en_posicion(posicion):
    if posicion < len(lista_alumnos_circo):
        alumno = lista_alumnos_circo[posicion]
        print(f"Nombre: {alumno['nombre']}, Apellido: {alumno['apellido']}, Edad: {alumno['edad']}")
    else:
        print("La posición especificada está fuera del rango de la lista.")

# Insertamos los datos de "Antoni" al final de la lista
insertar_alumno("Antoni", "Apellido_Antoni", 25)

# Eliminamos los datos de "Abel" si existen en la lista
eliminar_alumno("Abel")

# Buscamos y mostramos al alumno en la posición 4 de la lista
mostrar_alumno_en_posicion(4)

# 2. crear una lista con tres dicionarios donde tendran los datos de sus mascotas (nombre,edad,sexo,raza)

#tareas
#mostar lista con 4 diccionario
# editar el 3er registro y cambiarle la edad sin modificar la lista original
#mostrar lista original y luego la lista con la 3er registro