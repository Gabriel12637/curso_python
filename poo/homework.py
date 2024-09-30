# crear una clase banco 
# sus atributos seran nombre, apellido,dni, numero de cuentay saldo de inicial

# como metodo podemos hecer deposito retirar dinero y ver estaqdo de cuenta


class Banco:
    def _init_(self, nombre, apellido, dni, numero_cuenta, saldo_inicial=0):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

gabriel=Banco("gabriel","rodriguez","536372","4251652722","$1000")

class Banco:
    def __init__(self, nombre, apellido, dni, numero_cuenta, saldo_inicial=0):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad

    def ver_estado_cuenta(self):
        return f"{self.nombre} {self.apellido}: {self.saldo} €"

# Ejemplo de uso
cliente = Banco("Juan", "Pérez", "12345678A", "ES12345678901234567890", 1000)
print(cliente.ver_estado_cuenta())
cliente.depositar(500)
cliente.retirar(200)
print(cliente.ver_estado_cuenta())
  



# EJERCICIO 2
# crear una clase agencia
# con sus atributos nombre y apellido del pasajero dni numero del pasajero feche de viaje
# sus metodos seran ingresar origen,ingtresar destino,cancelar viaje,ver estado de pasaje


class Agencia:
    def __init__(self, nombre, apellido, dni, numero_pasajero, fecha_viaje):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_pasajero = numero_pasajero
        self.fecha_viaje = fecha_viaje
        self.origen = None
        self.destino = None

    def ingresar_origen(self, origen):
        self.origen = origen
    def ingresar_destino(self, destino):
        self.destino = destino
    def cancelar_viaje(self):
        self.origen = self.destino = None
    def ver_estado_pasaje(self):
        return f"{self.nombre} {self.apellido}, DNI: {self.dni}, Viaje: {self.fecha_viaje}, Origen: {self.origen or 'No ingresado'}, Destino: {self.destino or 'No ingresado'}"

# Ejemplo de uso
pasajero = Agencia("Ana", "García", "98765432B", "00123", "2024-10-15")
pasajero.ingresar_origen("Madrid")
pasajero.ingresar_destino("Barcelona")
print(pasajero.ver_estado_pasaje())
pasajero.cancelar_viaje()
print(pasajero.ver_estado_pasaje())