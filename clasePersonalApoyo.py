from claseAgente import Agente

class PersonalApoyo(Agente):
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.__categoria = categoria

    def calcular_sueldo(self):
        porcentaje_antiguedad = self.get_antiguedad() * 0.01 * self.get_sueldo_basico()
        return self.get_sueldo_basico() + porcentaje_antiguedad

    def __str__(self):
        return f"{super().__str__()}, Datos Personal: {self.__categoria}"
    
    def get_categoria(self):
        return self.__categoria
    
    def to_dict(self):
        # Obtener el diccionario de la superclase Agente
        agente_dict = super().to_dict()

        # Agregar el atributo propio de la clase PersonalApoyo
        agente_dict['categoria'] = self.__categoria

        return agente_dict
    
    