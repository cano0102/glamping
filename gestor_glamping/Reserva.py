from typing import List
from datetime import datetime
from gestor_glamping.alojamiento import Alojamiento
from gestor_glamping.Huesped import Huesped
from gestor_glamping.ServicioAdicional import ServicioAdicional
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
    
    def agregar_servicio(self, servicio: ServicioAdicional):
        self.__servicios_adicionales.append(servicio)
        print(f"Servicio '{servicio.mostrar_info()} agregado correctamente.")

    def calcular_precio_total(self, temporada: str = "baja"):
        # Calcular noches
        noches = self.calcular_noches()
        # Precio base del alojamiento según temporada
        precio_base = self.__alojamiento.get_price()
        if hasattr(self.__alojamiento, 'calcular_precio_temporada'):
            self.__alojamiento.calcular_precio_temporada(temporada)
            precio_base = self.__alojamiento.get_price()
        total_alojamiento = noches * precio_base
        # Sumar servicios adicionales
        total_servicios = sum(servicio._ServicioAdicional__precio for servicio in self.__servicios_adicionales)
        self.__precio_total = total_alojamiento + total_servicios
        return self.__precio_total
    
    def cambiar_estado(self, nuevo_estado: str):
        estados_validos = ["confirmada", "en_curso", "finalizada", "cancelada"]
        if nuevo_estado.lower() in estados_validos:
            self.set_state(nuevo_estado.lower())
            print(f"Estado de la reserva cambiado a: {nuevo_estado.lower()}")
        else:
            print("Estado no válido. Usa: confirmada, en_curso, finalizada o cancelada.")

            
    def mostrar_info(self):
       return (f"Código de reserva: {self.__codigo}, "
               f"Huésped: {self.__huesped}, "
               f"Alojamiento: {self.__alojamiento}, "
               f"Fecha de check-in: {self.__fecha_checkin}, "
               f"Fecha de check-out: {self.__fecha_checkout}, "
               f"Servicios adicionales: {', '.join(str(servicio) for servicio in self.__servicios_adicionales)}, "
               f"Precio total: {self.__precio_total}, "
               f"Estado: {self.__estado}")
