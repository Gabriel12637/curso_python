class personaje:
    #atributos
    def __init__(self,nombre,edad,usuario,bando,raza):
        self.nombre=nombre
        self.edad=edad
        self.usuario=usuario
        self.bando=bando
        self.raza=raza
    
luffy=personaje("luffy",18,"gomu gpmu no mi ","pirata","humano")
print(luffy.nombre)         
cobby=personaje("cobby",15,"no","sword","humano")
print(cobby.bando)
king=personaje("king",40,"zoan mitologica","pirata","linaria")
print(king.raza)
print(king.mostrar_personaje())