from flask import Flask, render_template, request
import servicios
import formularios

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    productos = [
        {'nombre': 'THE MONSTERS - Have a Seat Vinyl Plush Blind Box', 'precio': 1200.0, 'imagen': 'https://prod-global-static.oss-us-east-1.aliyuncs.com/globalAdmin/1720579884288____dada____.png?x-oss-process=image/format,webp'},
    ]
    return render_template('productos.html', lista = productos)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template('ejemplo1.html')

@app.route('/ejemplo2')
def ejemplo2():
    return render_template('ejemplo2.html')

@app.route('/hola')
def hola():
    return 'Hola, Mundo!'

@app.route('/usuario/<string:nombre>')
def usuario_nombre(nombre):
    return f'Hola, {nombre}!'

@app.route('/usuario/<int:id>/<string:nombre>')
def usuario_id_nombre(id, nombre):
    return f'El usuario {nombre} tiene el id {id}'

@app.route('/numero/<int:numero>')
def numero(numero):
    return f'El número es {numero}'

@app.route('/suma/<float:num1>/<float:num2>')
def suma(num1, num2):
    return f'La suma de {num1} y {num2} es {num1 + num2}'

@app.route('/default/')
@app.route('/default/<string:nombre>')
def default(nombre = 'valor por defecto'):
    return f'Hola, {nombre}!'

@app.route('/formulario')
def formulario():
    return '''
        <form>
            <div>
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre">
            </div>
            <div>
                <label for="apellido">Apellidos:</label>
                <input type="text" id="apellidos" name="apellidos">
            </div>
            <input type="submit" value="Enviar">
        </form>
    '''

@app.route('/calculadora')
def calculadora():
    return render_template('calculadora.html', num1=0.0, num2=0.0, operacion='+', resultado=None)

@app.route('/calculadora', methods=['POST'])
def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacion = request.form['operador']
    resultado = None
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == 'x':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2
    return render_template('calculadora.html', num1=num1, num2=num2, operacion=operacion, resultado=resultado)

@app.route('/cinepolis')
def cinepolis():
    return render_template('cinepolis.html', nombre='', compradores=None, tarjeta='no', boletos=None, total=None, error='')

@app.route('/cinepolis', methods=['POST'])
def total():
    nombre = request.form['nombre']
    compradores = int(request.form['compradores'])
    tarjeta = request.form['tarjeta']
    boletos = int(request.form['boletos'])
    
    max_boletos = 7 * compradores
    if boletos > max_boletos:
        error = 'No hay suficientes boletos, por favor modifique la cantidad de boletos o la cantidad de compradores'
        return render_template('cinepolis.html', nombre=nombre, compradores=compradores, tarjeta=tarjeta, boletos=boletos, total=None, error=error)

    servicio = servicios.Cinepolis(boletos, compradores, tarjeta)
    total = servicio.calcular_total()

    return render_template('cinepolis.html', nombre=nombre, compradores=compradores, tarjeta=tarjeta, boletos=boletos, total=total, error='')

@app.route('/alumnos', methods=['GET', 'POST'])
def alumnos():
    formulario = formularios.Alumno(request.form)
    if request.method == 'POST' and formulario.validate():
        alumno = {
            'matricula': formulario.matricula.data, 
            'nombre': formulario.nombre.data, 
            'apellidos': formulario.apellidos.data, 
            'email': formulario.email.data, 
            'password': formulario.password.data
            }
    else:
        alumno = None
    return render_template('alumnos.html', formulario=formulario, alumno=alumno)

@app.route('/zodiaco', methods=['GET', 'POST'])
def zodiaco():
    formulario = formularios.Zodiaco(request.form)
    if request.method == 'POST' and formulario.validate():
        zodiaco = {
            'nombre': formulario.nombre.data, 
            'apellido_paterno': formulario.apellido_paterno.data, 
            'apellido_materno': formulario.apellido_materno.data, 
            'fecha_nacimiento': formulario.fecha_nacimiento.data
            }
        
        servicio = servicios.Zodiaco(zodiaco['fecha_nacimiento'].strftime('%Y-%m-%d'))
        zodiaco['edad'] = servicio.calcular_edad()
        zodiaco['signo'] = servicio.calcular_signo()
    else:
        zodiaco = None
    return render_template('zodiaco.html', formulario=formulario, zodiaco=zodiaco)

if __name__ == '__main__':
    app.run(debug = True, port = 3000) 
    # debug = True recarga el servidor automáticamente
    # port = 3000 define el puerto en el que se ejecutará el servidor