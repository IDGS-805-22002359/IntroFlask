from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo = 'IDGS805 - Intro Flask'
    productos = [
        {'nombre': 'THE MONSTERS - Have a Seat Vinyl Plush Blind Box', 'precio': 1200.0, 'imagen': 'https://prod-global-static.oss-us-east-1.aliyuncs.com/globalAdmin/1720579884288____dada____.png?x-oss-process=image/format,webp'},
    ]
    return render_template('index.html', titulo = titulo, lista = productos)

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

if __name__ == '__main__':
    app.run(debug = True, port = 3000) 
    # debug = True recarga el servidor automáticamente
    # port = 3000 define el puerto en el que se ejecutará el servidor