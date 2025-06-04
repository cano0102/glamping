class Persona:
    def __init__(self, nombre, telefono, email, identificacion):
        self._nombre = nombre
        self.__telefono = telefono
        self._email = email
        self.__identificacion = identificacion

    def mostrar_info(self):
        return (f"Nombre: {self._nombre}, "
                f"Telefono: {self.__telefono}, "
                f"Email: {self._email}, "
                f"Identificacion: {self.__identificacion}")
