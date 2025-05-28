class Persona:
    def __init__(self, nombre, telefono, email, identificacion):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        self.__identificacion = identificacion

    def mostrar_info(self):
        return (f"Nombre: {self.__nombre}, "
                f"Telefono: {self.__telefono}, "
                f"Email: {self.__email}, "
                f"Identificacion: {self.__identificacion}")
