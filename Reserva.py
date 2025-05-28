from typing import List
from datetime import datetime
from alojamiento import Alojamiento
from Huesped import Huesped

class Reserva:
    _codigo_reserva = 1
    def __init__(self,huesped: Huesped,alojamiento: Alojamiento,fecha_checkin: str, fecha_checkout: str,servicios_adicionales: List[str]):
        # ATRIBUTOS DE INSTANCIA
        self.__codigo = Reserva._codigo_reserva
        Reserva._codigo_reserva += 1
        self.__huesped = huesped
        self.__alojamiento = alojamiento
        self.__fecha_checkin = fecha_checkin
        self.__fecha_checkout = fecha_checkout
        self.__servicios_adicionales = servicios_adicionales
        self.__precio_total = 0
        self.__estado = "confirmada"
        
    
    #GETTERS
    def get_services(self):
        return self.__servicios_adicionales
    
    def get_state(self):
        return self.__estado
    
    #SETTERS
    def set_services(self, service: str):
        self.__servicios_adicionales.append(service)
        
    def set_state(self,new_state: str):
        self.__estado = new_state

    def calcular_noches(self) -> int:
        """
        Calcula el número de noches entre la fecha de check-in y check-out.
        Las fechas deben estar en formato 'YYYY-MM-DD'.
        """
        checkin = datetime.strptime(self.__fecha_checkin, "%Y-%m-%d").date()
        checkout = datetime.strptime(self.__fecha_checkout, "%Y-%m-%d").date()
        return (checkout - checkin).days
    
    def agregar_servicio(self,servicio: str):
        ##FALTA POR EL OBJETO SERVICIO ADICIONAL
        self.set_services(servicio)
        print("Servicio agregado correctamente.")
        pass
    
    def calcular_precio_total(self):
        #FALTA POR EL OBJETO SERVICIO ADICIONAL
        pass
    
    def cambiar_estado(self, nuevo_estado: str):
        estados_validos = ["confirmada", "en_curso", "finalizada", "cancelada"]
        if nuevo_estado.lower() in estados_validos:
            self.set_state(nuevo_estado.lower())
            print(f"Estado de la reserva cambiado a: {nuevo_estado.lower()}")
        else:
            print("Estado no válido. Usa: confirmada, en_curso, finalizada o cancelada.")

            
    def mostrar_informacion(self):
        print(f"Código de reserva: {self.__codigo}")
        print(f"Huésped: {self.__huesped}")
        print(f"Alojamiento: {self.__alojamiento}")
        print(f"Fecha de check-in: {self.__fecha_checkin}")
        print(f"Fecha de check-out: {self.__fecha_checkout}")
        print(f"Servicios adicionales: {', '.join(self.__servicios_adicionales)}")
        print(f"Precio total: {self.__precio_total}")
        print(f"Estado: {self.__estado}")
