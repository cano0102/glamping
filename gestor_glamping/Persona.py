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
        # Getters y Setters para nombre
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, valor):
        self._nombre = valor

    # Getters y Setters para telefono
    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, valor):
        self.__telefono = valor

    # Getters y Setters para email
    def get_email(self):
        return self._email

    def set_email(self, valor):
        self._email = valor

    # Getters y Setters para identificacion
    def get_identificacion(self):
        return self.__identificacion

    def set_identificacion(self, valor):
        self.__identificacion = valor
    
