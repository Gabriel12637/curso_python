# crear una clase de alumnos con los atributos que usted crea por conveniencia
# luego instanciara a 4 alumnos
class alumnos:
    #atributos
    def __init__(self,nombre,edad,dni,programa,):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni
        self.programa=programa
        #metodos
        def escribir(self):
            print("estoy escribiendo")
        def tarea(self,nombre_docente):
            print("haciendo la tarea de:nombre_docente")
        def terminar_tarea(self):
            print("terminando tarea anterior")
            
juan=alumnos("juan","18","1627348","arquitectura de plataforma")
print(juan.nombre)  
carlos=alumnos("carlos","17","1957448","arquitectura de plataforma")
print(carlos.programa)
pancho=alumnos("pancho","18","1627428","arquitectura de plataforma")
print(pancho.dni)
rony=alumnos("rony","18","9734248","arquitectura de plataforma")
print(rony.edad)