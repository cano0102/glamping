from Persona import Persona
class Empleado(Persona):
    def __init__(self, nombre, telefono, email, identificacion,cargo,salario,fecha_ingreso):
        super().__init__(nombre, telefono, email, identificacion)
        self.__cargo = cargo
        self.__salario = salario
        self.__fecha_ingreso = fecha_ingreso

    def calcular_antiguedad(self):
        antiguedad = 2025 - int(self.__fecha_ingreso)
        return f"LA ANTIGUEDAD DEL EMPREAD@ ES DE {antiguedad}"

    def mostrar_info(self):
        return (f"Nombre: {self.__nombre}, "
                f"Telefono: {self.__telefono}, "
                f"Email: {self.__email}, "
                f"Identificacion: {self.__identificacion}, "
                f"Cargo: {self.__cargo}, "
                f"Salario: {self.__salario}, "
                f"Fecha_ingreso: {self.__fecha_ingreso}")
    
    def get_id(self):
        return self._identificacion  # Corrige el atributo la implementación


