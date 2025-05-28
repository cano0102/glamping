from alojamiento import Alojamiento
from Huesped import Huesped
from Empleado import Empleado
from Reserva import Reserva
from ServicioAdicional import ServicioAdicional
from glamping import Glamping

# Crear alojamientos
aloj1 = Alojamiento("cabaña", 4, 200.0, True, ["wifi", "chimenea"])
aloj2 = Alojamiento("domo", 2, 150.0, True, ["wifi", "jacuzzi"])
aloj3 = Alojamiento("tienda_lujo", 3, 180.0, True, ["wifi", "terraza"])

# Crear huéspedes
huesped1 = Huesped("Ana Perez", "123456789", "ana@email.com", "ID001", 1995, "Colombia", "Vegetariana")
huesped2 = Huesped("Luis Gomez", "987654321", "luis@email.com", "ID002", 1988, "México", "Sin preferencia")

# Crear empleados
empleado1 = Empleado("Carlos Ruiz", "5551234", "carlos@email.com", "EMP001", "Recepcionista", 1200, 2020)
empleado2 = Empleado("Maria Diaz", "5555678", "maria@email.com", "EMP002", "Limpieza", 1000, 2022)

# Crear servicios adicionales
spa = ServicioAdicional("Spa", "Masaje relajante", 50, 2)
tour = ServicioAdicional("Tour", "Caminata ecológica", 30, 3)
comida = ServicioAdicional("Comida Gourmet", "Cena especial", 40, 1)

# Crear listas iniciales
alojamientos = [aloj1, aloj2, aloj3]
huespedes = [huesped1, huesped2]
empleados = [empleado1, empleado2]
servicios = [spa, tour, comida]
reservas = []

# Crear instancia de Glamping
mi_glamping = Glamping("EcoGlamp", "Montaña Verde", alojamientos, huespedes, empleados, reservas, servicios)

# Crear una reserva
reserva1 = Reserva(huesped1, aloj1, "2025-06-01", "2025-06-05", [spa, comida])
reservas.append(reserva1)
aloj1.ocupar()  # Marcar alojamiento como ocupado

# Probar métodos
print("--- Información de la reserva ---")
reserva1.mostrar_informacion()
print(f"Noches reservadas: {reserva1.calcular_noches()}")
print(f"Precio total (baja): {reserva1.calcular_precio_total('baja')}")
print(f"Precio total (alta): {reserva1.calcular_precio_total('alta')}")

print("\n--- Ocupación actual ---")
print(f"Ocupación: {mi_glamping.calcular_ocupacion_actual():.2f}%")

print("\n--- Reservas activas ---")
for r in mi_glamping.listar_reservas_activas():
    r.mostrar_informacion()

print("\n--- Ingresos junio 2025 ---")
ingresos = mi_glamping.generar_reporte_ingresos_mes(6, 2025)
print(f"Ingresos en junio 2025: ${ingresos}")
# Crear una nueva reserva para aumentar la ocupación
reserva2 = Reserva(huesped2, aloj2, "2025-06-02", "2025-06-06", [tour])
reservas.append(reserva2)
aloj2.ocupar()  # Marcar alojamiento como ocupado

print("\n--- Nueva reserva creada ---")
reserva2.mostrar_informacion()

print("\n--- Ocupación actual actualizada ---")
print(f"Ocupación: {mi_glamping.calcular_ocupacion_actual():.2f}%")