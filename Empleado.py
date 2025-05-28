class Empleado (Persona):
    def __init__(self, nombre, telefono, email, identificacion,cargo,salario,fecha_ingreso):
        super().__init__(nombre, telefono, email, identificacion)
        self._cargo = cargo,
        self._salario = salario,
        self._fecha_ingreso =fecha_ingreso

    def calcular_antiguedad():
        pass

    def mostrar_info():
        pass


