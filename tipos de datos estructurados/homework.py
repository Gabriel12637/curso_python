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
    for alumno in "lista_alumnos":
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
# como dueño de mi mascota 
# deseo ver una lista de mis mascotas
# para tener un resumen o control de ellos
# yo como dueño de mi mascota
# deseo actualizar la edad de mis mascota
#para tener una lista de mis mascotas
dato_mascota=[
    {"nombre":"michu",
     "edad":5,
     "sexo":"macho",
     "raza":"siames"
     },
    {"nombre":"luna",
     "edad":6,
     "sexo":"hembra",
     "raza":"persa"
     },
    {"nombre":"mimi",
     "edad":4,
     "sexo":"hembra",
     "raza":"angora"
     },
    {"nombre":"gato",
     "edad":7,
     "sexo":"macho",
     "raza":"britanico"
     }
]

for diccionario in dato_mascota:
    print(diccionario)
print()
copia_mascotas=dato_mascota.copy()
copia_mascotas[2]["edad"]=7
for copy in copia_mascotas:
    print(copy)




    # Crear una lista con tres diccionarios que contengan los datos de las mascotas
mascotas = [
    {"nombre": "Max", "edad": 3, "sexo": "macho", "raza": "Labrador"},
    {"nombre": "Luna", "edad": 2, "sexo": "hembra", "raza": "Golden Retriever"},
    {"nombre": "Buddy", "edad": 4, "sexo": "macho", "raza": "Poodle"}
]

# Mostrar la lista original
print("Lista original:")
for mascota in mascotas:
    print(mascota)

# Crear una copia de la lista original para no modificarla
mascotas_copia = mascotas[:]

# Editar el tercer registro cambiando la edad sin modificar la lista original
mascotas_copia[2]["edad"] = 5

# Mostrar la lista original y la lista con el tercer registro modificado
print("\nLista original:")
for mascota in mascotas:
    print(mascota)

print("\nLista con el tercer registro modificado:")
for mascota in mascotas_copia:
    print(mascota)

# Crear una lista de tus mascotas
mis_mascotas = [mascota["nombre"] for mascota in mascotas]

# Mostrar la lista de tus mascotas
print("\nMis mascotas:")
print(mis_mascotas)




# Crear una lista con tres diccionarios que contienen los datos de las mascotas
mascotas = [
    {"nombre": "Max", "edad": 3, "sexo": "macho", "raza": "Labrador"},
    {"nombre": "Luna", "edad": 2, "sexo": "hembra", "raza": "Golden Retriever"},
    {"nombre": "Buddy", "edad": 4, "sexo": "macho", "raza": "Poodle"}
]

# Agregar un cuarto diccionario a la lista
mascotas.append({"nombre": "Coco", "edad": 1, "sexo": "hembra", "raza": "Chihuahua"})

# Mostrar la lista con el cuarto diccionario
print("Lista con el cuarto diccionario:")
for mascota in mascotas:
    print(mascota)

# Crear una copia de la lista original para no modificarla
mascotas_copia = mascotas[:]

# Editar el tercer registro cambiando la edad sin modificar la lista original
mascotas_copia[2]["edad"] = 5

# Mostrar la lista original y la lista con el tercer registro modificado
print("\nLista original:")
for mascota in mascotas:
    print(mascota)

print("\nLista con el tercer registro modificado:")
for mascota in mascotas_copia:
    print(mascota)

# Crear una lista de tus mascotas
mis_mascotas = [mascota["nombre"] for mascota in mascotas]

# Mostrar la lista de tus mascotas
print("\nMis mascotas:")
print(mis_mascotas)

# Actualizar la edad de tus mascotas
nombre_mascota = "Max"  # Nombre de la mascota a actualizar
nueva_edad = 4  # Nueva edad de la mascota

for mascota in mascotas:
    if mascota["nombre"] == nombre_mascota:
        mascota["edad"] = nueva_edad

# Mostrar la lista actualizada de tus mascotas
print("\nLista actualizada de mis mascotas:")
for mascota in mascotas:
    print(mascota)




# el director del tecnologico jose maria arguedas
# un docente desea actualizar el proceso de registro de notas de sus alumnos con las siguientes aclaraciones 
#los docentes podran poner la nota pero no podran editarlo
#solo los coordinadores de programa de estudio podran dar el acceso de edicion de nota previa
#peticion del docente encargado 
#los estudiantes solo podran ver su nota y porsentage de asistencia. 

# yo como docente
#voy a actualizar las notas
#para su  registro de sus notas  


# un emperesari de alquiler de motos deasea guardar en una base de datos la informacion 
# de sus vehiculos ,proceso que desea automatisar con un sistema informatico
# las acciones que ouede realizar el empresario son ver las listas de autos 
# que tiene , podra tambien actualizar la lista y agregar un nuevo veiculo 
# casos de uso
 # caso de uso 
# yo como empresario podfre ver la 
# informacion de los veiculos

# programacion 
class AlquilerMotos:
    def __init__(self):
        self.vehiculos = []

    def ver_vehiculos(self):
        if self.vehiculos:
            for vehiculo in self.vehiculos:
                print(vehiculo)
        else:
            print("No hay vehículos disponibles.")

    def agregar_vehiculo(self, marca, modelo, año):
        self.vehiculos.append({"Marca": marca, "Modelo": modelo, "Año": año, "Disponible": True})
        print("Vehículo agregado con éxito.")

    def actualizar_disponibilidad(self, vehiculo_index, disponible):
        if 0 <= vehiculo_index < len(self.vehiculos):
            self.vehiculos[vehiculo_index]["Disponible"] = disponible
            print("Disponibilidad actualizada con éxito.")
        else:
            print("Índice de vehículo fuera de rango.")

# Uso del sistema
if __name__ == "__main__":
    sistema = AlquilerMotos()

    # Ejemplo de uso
    sistema.agregar_vehiculo("Honda", "CBR500R", 2022)
    sistema.agregar_vehiculo("Yamaha", "YZF-R3", 2021)
    sistema.ver_vehiculos()
    sistema.actualizar_disponibilidad(0, False)
    sistema.ver_vehiculos()

