def mayor_edad(edad):
    """funcion para subir si es una persona mayor de edad
    """
    if edad>=18:
        print("es mator de edad")
    else:
        print("es menor de edad")
def es_mayor(lista):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > mayor:
            mayor=n
    return mayor