from typing import List

class Alojamiento:
    _numero = 1

    def __init__(self, tipo: str, capacidad_maxima: int, precio_base_noche: float, disponible: bool, amenidades: List[str]):
        # ATRIBUTOS DE CLASE
        self.__numero = Alojamiento._numero
        Alojamiento._numero += 1
        self.__tipo = tipo
        self.__capacidad_maxima = capacidad_maxima
        self.__precio_base_noche = precio_base_noche
        self.__disponible = disponible
        self.__amenidades = amenidades

    def mostrar_info(self):
        return (f"Alojamiento #{self.__numero} - Tipo: {self.__tipo}, "
                f"Capacidad: {self.__capacidad_maxima}, "
                f"Precio base: {self.__precio_base_noche}$, "
                f"Amenidades: {', '.join(self.__amenidades)}, "
                f"Disponible: {'Sí' if self.__disponible else 'No'}")
    
    def __str__(self):
        return f"{self.__tipo} - Capacidad: {self.__capacidad_maxima}, Precio: {self.__precio_base_noche}$"


    # GETTERS
    def get_price(self):
        # GETTER DEL PRECIO DEL ALOJAMIENTO
        return self.__precio_base_noche

    def get_disponible(self):
        return self.__disponible

    def get_id(self):
        return self.__nombre  # Cambia esto por el atributo correcto de id en Huesped

    def get_numero(self):
        return self.__numero

    def get_tipo(self):
        return self.__tipo

    def esta_disponible(self, fecha_in, fecha_out):
        return self.__disponible

    # SETTERS
    def set_price(self, nuevo_valor: int):
        # SETTER DEL PRECIO DEL ALOJAMIENTO
        self.__precio_base_noche = nuevo_valor

    def set_disponibilidad(self, nuevo_valor: bool):
        self.__disponible = nuevo_valor

    def ocupar(self):
        self.__disponible = False

    def liberar(self):
        self.__disponible = True

    def calcular_precio_temporada(self, temporada: str):
        precio = self.get_price()
        temporada = temporada.capitalize()
        if temporada == "Alta":
            self.set_price(precio + (precio * 30) / 100)
            print(f"Temporada alta se ha aumentado su costo al 30% con un valor final de {self.get_price()}$")
        elif temporada == "Media":
            self.set_price(precio + (precio * 10) / 100)
            print(f"Temporada media se ha aumentado su costo al 10% con un valor final de {self.get_price()}$")
        else:
            print(f"Temporada baja con un valor final de {self.get_price()}$")
        
    def Reservar(self):
        if self.get_disponible():  
            self.set_disponibilidad(False)  
            print("Reserva hecha correctamente.")
        else:
            print("Alojamiento no disponible.")

    def Liberar(self):
        if not self.get_disponible():  
            self.set_disponibilidad(True) 
            print("Reserva liberada correctamente.")
        else:
            print("El alojamiento ya está libre.")
