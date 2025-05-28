class Huesped:

    def __init__(self, nombre, telefono, email, identificacion,fecha_nacimiento,pais_origen,preferencias_alimentarias):
        super().__init__(nombre, telefono, email, identificacion)
        self.__fecha_nacimiento = fecha_nacimiento,
        self.__pais_origen =pais_origen,
        self.__preferencias_alimentarias = preferencias_alimentarias
    
    def calcular_edad(self):

        edad =   2025 - self.__fecha_nacimiento
        f"LA EDAD DE LA HUESPED ES DE: {edad}"

        
    def mostrar_info(self):
        return (f"Nombre {self.__nombre} , "
                f"Telefono: {self.__telefono}, "
                f"Email: {self.__email}$, "
                f"Identificacion: {self.__identificacion}, "
                f"Fecha_nacimiento: {self._fecha_nacimiento}"
                f"Origen: {self.__pais_origen}"
                f"Preferencias_alimentarias: {self.__preferencias_alimentarias }")
            
        