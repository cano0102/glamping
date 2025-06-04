from gestor_glamping.Persona import Persona
class Huesped(Persona):
    def __init__(self, nombre, telefono, email, identificacion, fecha_nacimiento, pais_origen, preferencias_alimentarias):
        super().__init__(nombre, telefono, email, identificacion)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__pais_origen = pais_origen
        self.__preferencias_alimentarias = preferencias_alimentarias
    def __str__(self):
        return f"{self._nombre} ({self._email})"

    
    def calcular_edad(self):
        # Suponiendo que fecha_nacimiento es un año (int)
        return 2025 - int(self.__fecha_nacimiento)

        
    def mostrar_info(self):
        return (f"Nombre: {self.__nombre}, "
                f"Telefono: {self.__telefono}, "
                f"Email: {self.__email}, "
                f"Identificacion: {self.__identificacion}, "
                f"Fecha_nacimiento: {self.__fecha_nacimiento}, "
                f"Origen: {self.__pais_origen}, "
                f"Preferencias alimentarias: {self.__preferencias_alimentarias}")
    
    def get_id(self):
        return self._identificacion  # Corrige el atributo según tu implementación

