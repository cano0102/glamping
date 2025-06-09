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
    
     # Getters
    def get_nombre(self):
        return self._nombre
    
    def get_telefono(self):
        return self._telefono
    
    def get_email(self):
        return self._email
    
    def get_id(self):
        return self._identificacion
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def get_pais_origen(self):
        return self.__pais_origen
    
    def get_preferencias_alimentarias(self):
        return self.__preferencias_alimentarias
    

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_email(self, email):
        self._email = email

    def set_id(self, identificacion):
        self._identificacion = identificacion

    # Setters
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_pais_origen(self, pais_origen):
        self.__pais_origen = pais_origen

    def set_preferencias_alimentarias(self, preferencias_alimentarias):
        self.__preferencias_alimentarias = preferencias_alimentarias
    