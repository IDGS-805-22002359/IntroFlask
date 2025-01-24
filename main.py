from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hola')
def hola():
    return 'Hola, Mundo!'

if __name__ == '__main__':
    app.run(debug = True, port = 3000) 
    # debug = True will automatically reload the server when you make changes to the code
    # port = 3000 will run the server on port 3000