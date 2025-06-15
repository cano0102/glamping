class ServicioAdicional:
    def __init__(self, nombre, descripcion, precio, duracion_horas):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__duracion_horas = duracion_horas

    def __str__(self):
        return (f"Servicio: {self.__nombre}, "
                f"Descripción: {self.__descripcion}, "
                f"Precio: {self.__precio}, "
                f"Duración: {self.__duracion_horas} horas")

    def mostrar_info(self):
        return (f"Servicio: {self.__nombre}, "
                f"Descripción: {self.__descripcion}, "
                f"Precio: {self.__precio}, "
                f"Duración: {self.__duracion_horas} horas")

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def get_precio(self):
        return self.__precio

    def get_duracion_horas(self):
        return self.__duracion_horas

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_precio(self, precio):
        self.__precio = precio

    def set_duracion_horas(self, duracion_horas):
        self.__duracion_horas = duracion_horas