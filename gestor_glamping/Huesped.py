from gestor_glamping.Persona import Persona

class Huesped(Persona):
    def __init__(self, nombre, telefono, email, identificacion, fecha_nacimiento, pais_origen, preferencias_alimentarias):
        super().__init__(nombre, telefono, email, identificacion)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__pais_origen = pais_origen
        self.__preferencias_alimentarias = preferencias_alimentarias

    def __str__(self):
        # Usa los getters, no accedas a atributos directamente
        return f"{self.get_nombre()} ({self.get_email()})"

    def calcular_edad(self):
        return 2025 - int(self.__fecha_nacimiento)

    def mostrar_info(self):
        return (f"Nombre: {self.get_nombre()}, "
                f"Telefono: {self.get_telefono()}, "
                f"Email: {self.get_email()}, "
                f"Identificacion: {self.get_identificacion()}, "
                f"Fecha_nacimiento: {self.__fecha_nacimiento}, "
                f"Origen: {self.__pais_origen}, "
                f"Preferencias alimentarias: {self.__preferencias_alimentarias}")

    # Getters y setters para los nuevos atributos
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_pais_origen(self):
        return self.__pais_origen

    def get_preferencias_alimentarias(self):
        return self.__preferencias_alimentarias

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_pais_origen(self, pais_origen):
        self.__pais_origen = pais_origen

    def set_preferencias_alimentarias(self, preferencias_alimentarias):
        self.__preferencias_alimentarias = preferencias_alimentarias