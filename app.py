from flask import Flask,render_template, request, redirect, url_for
from gestor_glamping.Persona import Persona
from gestor_glamping.Huesped import Huesped
from gestor_glamping.Empleado import Empleado
from gestor_glamping.alojamiento import Alojamiento
from gestor_glamping.Reserva import Reserva
from gestor_glamping.ServicioAdicional import ServicioAdicional



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/persona', methods=['GET', 'POST'])
def persona():
    info = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        identificacion = request.form['identificacion']

        persona = Persona(nombre, telefono, email, identificacion)
        info = persona.mostrar_info()

    return render_template('persona.html', info=info)


@app.route('/huesped', methods=['GET', 'POST'])
def huesped():
    info = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        identificacion = request.form['identificacion']
        fecha_nacimiento = request.form['fecha_nacimiento']
        pais_origen = request.form['pais_origen']
        preferencias = request.form['preferencias']
        huesped = Huesped(nombre, telefono, email, identificacion, fecha_nacimiento, pais_origen, preferencias)
        info = huesped.mostrar_info()
    return render_template('huesped.html', info=info)


@app.route('/empleado', methods=['GET', 'POST'])
def empleado():
    info = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        identificacion = request.form['identificacion']
        cargo = request.form['cargo']
        salario = request.form['salario']
        fecha_ingreso = request.form['fecha_ingreso']
        empleado = Empleado(nombre, telefono, email, identificacion, cargo, salario, fecha_ingreso)
        info = empleado.mostrar_info()
    return render_template('empleado.html', info=info)


@app.route('/alojamiento', methods=['GET', 'POST'])
def alojamiento():
    info = ''
    if request.method == 'POST':
        tipo = request.form['tipo']
        capacidad_maxima = int(request.form['capacidad_maxima'])
        precio_base_noche = float(request.form['precio_base_noche'])
        disponible = request.form.get('disponible') == 'on'
        amenidades = request.form['amenidades'].split(',')  # Separadas por coma
        alojamiento = Alojamiento(tipo, capacidad_maxima, precio_base_noche, disponible, amenidades)
        info = alojamiento.mostrar_info()
    return render_template('alojamiento.html', info=info)



@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    info = ''
    if request.method == 'POST':
        # Aquí deberías obtener los objetos reales de Huesped y Alojamiento según tu lógica
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        identificacion = request.form['identificacion']
        huesped = Huesped(nombre, telefono, email, identificacion, '', '', '')
        tipo = request.form['tipo']
        capacidad_maxima = int(request.form['capacidad_maxima'])
        precio_base_noche = float(request.form['precio_base_noche'])
        disponible = True
        amenidades = []
        alojamiento = Alojamiento(tipo, capacidad_maxima, precio_base_noche, disponible, amenidades)
        fecha_checkin = request.form['fecha_checkin']
        fecha_checkout = request.form['fecha_checkout']
        servicios_adicionales = request.form['servicios_adicionales'].split(',') if request.form['servicios_adicionales'] else []
        reserva = Reserva(huesped, alojamiento, fecha_checkin, fecha_checkout, servicios_adicionales)
        info = reserva.mostrar_info()
    return render_template('reserva.html', info=info)

@app.route('/servicio', methods=['GET', 'POST'])
def servicio():
    info = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        precio = float(request.form['precio'])
        duracion_horas = float(request.form['duracion_horas'])
        servicio = ServicioAdicional(nombre, descripcion, precio, duracion_horas)
        info = f"Servicio registrado: {servicio}"
    return render_template('servicio.html', info=info)

@app.route('/build/html/<path:filename>')
def sphinx_static(filename):
    return send_from_directory('build/html', filename)

@app.route('/_static/<path:filename>')
def sphinx_static_files(filename):
    return send_from_directory('build/html/_static', filename)

@app.route('/Documentacion')
def documentacion():
    return redirect('/build/html/index.html')


if __name__ == '__main__':
    app.run(debug=True)
