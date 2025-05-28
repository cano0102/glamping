class ServicioAdicional:

    def __init__(self, nombre, descripcion, precio, duracion_horas):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__duracion_horas = duracion_horas

    def mostrar_info(self):
        return( f"Nombre : {self.__nombre}"
                f"Descripcion: {self.__descripcion}"
                f"Precio :{self.___precio}"
                f"Duracion horas: {self.__duracion_horas}")
