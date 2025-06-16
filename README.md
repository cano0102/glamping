# Sistema de Gestión de Glamping

Este proyecto es una aplicación en Python que implementa los conceptos fundamentales de la Programación Orientada a Objetos (POO) para gestionar un glamping. El sistema permite administrar alojamientos, huéspedes, empleados, reservas y servicios adicionales, integrando encapsulamiento, herencia y polimorfismo. Además, cuenta con una interfaz web básica usando Flask.

## Estructura del Proyecto

```
glamping/
│
├── app.py
├── gestor_glamping/
│   ├── Persona.py
│   ├── Huesped.py
│   ├── Empleado.py
│   ├── alojamiento.py
│   ├── Reserva.py
│   └── ServicioAdicional.py
├── README.md
└── docs/ (se crea al documentar con Sphinx)
```

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
- Interfaz web básica con Flask (`app.py`)

## Ejecución

1. Instala las dependencias necesarias (Flask y Sphinx para documentación):
   ```bash
   pip install flask sphinx
   ```

2. Ejecuta la aplicación web:
   ```bash
   python app.py
   ```
   Accede a `http://localhost:5000` en tu navegador.

## Requisitos Técnicos

- Python 3.x
- Flask (para la interfaz web)
- Sphinx (para la documentación)
- No requiere otras librerías externas

## Documentación automática con Sphinx

Este proyecto utiliza **Sphinx** para generar documentación automática a partir del código fuente y los docstrings.

### Pasos para generar la documentación:

1. Instala Sphinx si no lo tienes:
   ```bash
   pip install sphinx
   ```

2. Inicializa la documentación (solo la primera vez):
   ```bash
   sphinx-quickstart docs
   ```

3. Dentro del directorio `docs/source`, edita `conf.py` y asegúrate de tener:
   ```python
   extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']
   language = 'es'
   ```

4. Genera los archivos `.rst` automáticamente desde el código:
   ```bash
   sphinx-apidoc -o docs/source gestor_glamping
   ```

5. Construye la documentación en HTML:
   ```bash
   cd docs
   make html
   ```

6. Abre `docs/_build/html/index.html` en tu navegador para ver la documentación.

---

Este README describe la estructura y funcionamiento general del sistema de gestión de glamping, facilitando su comprensión, uso y documentación.
