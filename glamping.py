from alojamiento import Alojamiento
from Huesped import Huesped
from Empleado import Empleado
from Reserva import Reserva
from ServicioAdicional import ServicioAdicional
from typing import List
from datetime import datetime

class Glamping:
    def __init__(self,nombre: str,ubicacion: str, alojamientos: List[Alojamiento], huespedes: List[Huesped], empleados: List[Empleado],reservas:List[Reserva], servicios_disponibles: List[ServicioAdicional]):
        self.__nombre = nombre
        self.__ubicacion = ubicacion
        self.__alojamientos = alojamientos
        self.__huespedes = huespedes
        self.__empleados = empleados
        self.__reservas = reservas
        self.__servicios_disponibles = servicios_disponibles
        
    def get_nombre(self) -> str:
        return self.__nombre

    def get_ubicacion(self) -> str:
        return self.__ubicacion

    def get_alojamientos(self) -> List[Alojamiento]:
        return self.__alojamientos

    def get_huespedes(self) -> List[Huesped]:
        return self.__huespedes

    def get_empleados(self) -> List[Empleado]:
        return self.__empleados

    def get_reservas(self) -> List[Reserva]:
        return self.__reservas

    def get_servicios_disponibles(self) -> List[ServicioAdicional]:
        return self.__servicios_disponibles
    
    
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_ubicacion(self, ubicacion: str) -> None:
        self.__ubicacion = ubicacion

    def set_alojamientos(self, alojamientos: List[Alojamiento]) -> None:
        self.__alojamientos = alojamientos

    def set_huespedes(self, huespedes: List[Huesped]) -> None:
        self.__huespedes = huespedes

    def set_empleados(self, empleados: List[Empleado]) -> None:
        self.__empleados = empleados

    def set_reservas(self, reservas: List[Reserva]) -> None:
        self.__reservas = reservas

    def set_servicios_disponibles(self, servicios_disponibles: List[ServicioAdicional]) -> None:
        self.__servicios_disponibles = servicios_disponibles
        
    def agrega_alojamiento(self,alojamiento:Alojamiento):
        self.__alojamientos.append(alojamiento)
    
    def registrar_huesped(self,huesped:Huesped):
        self.__huespedes.append(huesped)
        
    def contratar_empleado(self,empleado:Empleado):
        self.__empleados.append(empleado)
        
    def crear_reserva(self,huesped_id,alojamiento_num,fecha_in,fecha_out):
        for huesped in self.__huespedes:
            if huesped.get_id() == huesped_id:
                for alojamiento in self.__alojamientos:
                    if alojamiento.get_numero() == alojamiento_num:
                        reserva = Reserva(huesped, alojamiento, fecha_in, fecha_out)
                        self.__reservas.append(reserva)
                        return reserva
        return None
    
    def buscar_alojamiento_disponible(self,tipo,fecha_in,fecha_out):
        for alojamiento in self.__alojamientos:
            if alojamiento.get_tipo() == tipo and alojamiento.esta_disponible(fecha_in, fecha_out):
                return alojamiento
        return None
    
    def calcular_ocupacion_actual(self) -> float:
        """
        Retorna el porcentaje de alojamientos ocupados actualmente.
        """
        if not self.__alojamientos:
            return 0.0
        ocupados = sum(1 for a in self.__alojamientos if not a.get_disponible())
        return (ocupados / len(self.__alojamientos)) * 100

    def listar_reservas_activas(self) -> list:
        """
        Retorna una lista de reservas cuyo estado es 'confirmada' o 'en_curso'.
        """
        return [r for r in self.__reservas if r.get_state() in ("confirmada", "en_curso")]

    def generar_reporte_ingresos_mes(self, mes: int, anio: int) -> float:
        """
        Suma el precio total de las reservas con check-in en el mes y año dados.
        """
        total = 0.0
        for reserva in self.__reservas:
            fecha_checkin = reserva._Reserva__fecha_checkin  # Acceso privado
            try:
                fecha = datetime.strptime(fecha_checkin, "%Y-%m-%d")
                if fecha.month == mes and fecha.year == anio:
                    total += reserva.calcular_precio_total()
            except Exception:
                continue
        return total



