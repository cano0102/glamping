# Sistema de Gestión de Glamping

Este proyecto es una aplicación básica en Python que implementa los conceptos fundamentales de la Programación Orientada a Objetos (POO) para gestionar un glamping. El sistema permite administrar alojamientos, huéspedes, empleados, reservas y servicios adicionales, integrando encapsulamiento, herencia y polimorfismo.

## Estructura de Clases

### 1. Persona (Clase base)
- **Atributos:** nombre, teléfono, email, identificación (privados)
- **Métodos:** Constructor, getters/setters, mostrar_info()

### 2. Huesped (Hereda de Persona)
- **Atributos adicionales:** fecha_nacimiento, país_origen, preferencias_alimentarias (privados)
- **Métodos:** Constructor, calcular_edad(), mostrar_info() sobrescrito

### 3. Empleado (Hereda de Persona)
- **Atributos adicionales:** cargo, salario, fecha_ingreso (privados)
- **Métodos:** Constructor, calcular_antiguedad(), mostrar_info() personalizado

### 4. Alojamiento
- **Atributos:** número, tipo, capacidad_maxima, precio_base_noche, amenidades (lista), disponible (privados)
- **Métodos:** Constructor, getters/setters, calcular_precio_temporada(), reservar(), liberar(), mostrar_info()

### 5. ServicioAdicional
- **Atributos:** nombre, descripción, precio, duración_horas (privados)
- **Métodos:** Constructor, getters/setters, mostrar_info()

### 6. Reserva
- **Atributos:** código_reserva, huesped, alojamiento, fecha_checkin, fecha_checkout, servicios_adicionales (lista), precio_total, estado (privados)
- **Métodos:** Constructor, calcular_noches(), agregar_servicio(), calcular_precio_total(), cambiar_estado(), mostrar_info()

### 7. Glamping
- **Atributos:** nombre, ubicación, alojamientos (lista), huespedes (lista), empleados (lista), reservas (lista), servicios_disponibles (lista) (privados)
- **Métodos:** Constructor, agregar_alojamiento(), registrar_huesped(), contratar_empleado(), crear_reserva(), buscar_alojamiento_disponible(), calcular_ocupacion_actual(), listar_reservas_activas(), generar_reporte_ingresos_mes()

## Funcionalidades Principales
- Registrar diferentes tipos de alojamientos (cabañas, domos, tiendas de lujo)
- Gestionar información de huéspedes y empleados
- Realizar y controlar reservas
- Calcular tarifas según temporada y tipo de alojamiento
- Ofrecer servicios adicionales (spa, tours, comidas)

## Ejecución
1. Define los objetos y relaciones entre clases en `glamping.py`.
2. Usa los métodos de la clase `Glamping` para gestionar el sistema.
3. El sistema permite registrar, consultar y modificar la información de alojamientos, huéspedes, empleados, reservas y servicios.

## Requisitos Técnicos
- Python 3.x
- No requiere librerías externas

## Notas
- El proyecto es modular y fácilmente ampliable.
- Cada clase implementa encapsulamiento y, donde corresponde, herencia y polimorfismo.

---

Este README describe la estructura y funcionamiento general del sistema de gestión de glamping, facilitando su comprensión y uso.
