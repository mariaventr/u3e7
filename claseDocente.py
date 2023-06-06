from claseAgente import Agente

class Docente(Agente):
    __carrera=''
    __cargo=''
    __catedra=''
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion='', tipo_investigacion=''):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    
    def calcular_sueldo(self):
        porcentaje_antiguedad = super().get_antiguedad() * 0.01 * super().get_sueldo_basico()
        porcentaje_cargo = 0.1 if self.__cargo == "simple" else 0.2 if self.__cargo == "semiexclusivo" else 0.5
        return super().get_sueldo_basico() + porcentaje_antiguedad + (porcentaje_cargo * super().get_sueldo_basico())

    def __str__(self):
        return f"{super().__str__()}. Datos Docente: {self.__carrera}, {self.__cargo},{self.__catedra}"
    
    def get_carrera(self):
        return self.__carrera
    
    def get_cargo(self):
        return self.__cargo
    
    def get_catedra(self):
        return self.__catedra
    
    def to_dict(self):
        # Obtener el diccionario de la superclase Agente
        agente_dict = super().to_dict()

        # Agregar los atributos propios de la clase Docente
        agente_dict['carrera'] = self.__carrera
        agente_dict['cargo'] = self.__cargo
        agente_dict['catedra'] = self.__catedra

        return agente_dict
    