from gestor_glamping.Persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, telefono, email, identificacion, cargo, salario, fecha_ingreso):
        super().__init__(nombre, telefono, email, identificacion)
        self.__cargo = cargo
        self.__salario = salario
        self.__fecha_ingreso = fecha_ingreso

    def calcular_antiguedad(self):
        antiguedad = 2025 - int(self.__fecha_ingreso)
        return f"La antigüedad del empleado es de {antiguedad} años"

    def mostrar_info(self):
        return (f"Nombre: {self.get_nombre()}, "
                f"Telefono: {self.get_telefono()}, "
                f"Email: {self.get_email()}, "
                f"Identificacion: {self.get_identificacion()}, "
                f"Cargo: {self.__cargo}, "
                f"Salario: {self.__salario}, "
                f"Fecha de ingreso: {self.__fecha_ingreso}")

    # Getters
    def get_cargo(self):
        return self.__cargo

    def get_salario(self):
        return self.__salario

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    # Setters
    def set_cargo(self, cargo):
        self.__cargo = cargo

    def set_salario(self, salario):
        self.__salario = salario

    def set_fecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso