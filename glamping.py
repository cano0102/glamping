class Persona:

    def __init__(self, nombre, telefono ,email, identificacion):
        self._nombre = nombre,
        self._telefono = telefono,
        self._email = email,
        self._identificacion = identificacion
        
        
        def mostrar_info():
            pass
        
class Huesped (Persona):

    def __init__(self, nombre, telefono, email, identificacion,fecha_nacimiento,pais_origen,preferencias_alimentarias):
        super().__init__(nombre, telefono, email, identificacion)
        self._fecha_nacimiento = fecha_nacimiento,
        self._pais_origen =pais_origen,
        self._preferencias_alimentarias = preferencias_alimentarias
    
    def calcular_edad():
        pass
    
    def mostrar_info():
        pass

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
