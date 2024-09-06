class Vehiculo:
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.numero_ruedas = numero_ruedas
        
    def Ver(self):
        return f"Marca : {self.marca}  Modelo : { self.modelo}  Numero de Ruedas : { self.numero_ruedas}"
        
class Automovil(Vehiculo):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,velocidad:int ,cilindrada:int ):
        super().__init__(marca, modelo, numero_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    

class AutomovilPasajeros(Automovil):
     def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,velocidad:int ,cilindrada:int ,numero_puestos:int):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.numero_puestos = numero_puestos


class AutomovilCarga(Automovil):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,velocidad:int ,cilindrada:int ,carga_kg:int):
        super().__init__(marca, modelo, numero_ruedas, velocidad, cilindrada)
        self.carga_kg = carga_kg
        
class Bicicleta(Vehiculo):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,tipo_bicicleta:str ) -> None:
        super().__init__(marca, modelo, numero_ruedas)
        self.tipo_bicicleta = tipo_bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca:str ,modelo:str ,numero_ruedas:int ,tipo_bicicleta:str ,nro_radios:int ,cuadro:str ,motor:str ):
        super().__init__(marca, modelo, numero_ruedas, tipo_bicicleta )
        self.nro_radios = nro_radios
        self.cuadro = cuadro
        self.motor = motor
    