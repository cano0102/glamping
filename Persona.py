class Persona:

    def __init__(self, nombre, telefono ,email, identificacion):
        self._nombre = nombre,
        self._telefono = telefono,
        self._email = email,
        self._identificacion = identificacion
        
        
        def mostrar_info(self):
            return (f"Nombre {self.__nombre} , "
                    f"Telefono: {self.__telefono}, "
                    f"Email: {self.__email}$, "
                    f"Identificacion: {self.__identificacion}, ")
