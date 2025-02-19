from datetime import datetime

class Cinepolis:
    def __init__(self, boletos, compradores, tarjeta):
        self.boletos = boletos
        self.compradores = compradores
        self.tarjeta = tarjeta
        self.maxBoletos = 7
        self.precioBoleto = 12
        self.descuento = 0
        self.total = 0

    def calcular_descuento(self):
        if self.boletos > 5:
            self.descuento = 0.15
        elif self.boletos <= 5 and self.boletos >= 3:
            self.descuento = 0.10

    def calcular_total(self):
        self.calcular_descuento()
        total = (self.boletos * self.precioBoleto) - (self.boletos * self.precioBoleto * self.descuento)
        if self.tarjeta == 'si':
            total = total - (total * 0.10)
        self.total = total
        return self.total

class Zodiaco:
    def __init__(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def calcular_edad(self):
        hoy = datetime.today()
        cumpleanios = datetime.strptime(self.fecha_nacimiento, '%Y-%m-%d')
        edad = hoy.year - cumpleanios.year - ((hoy.month, hoy.day) < (cumpleanios.month, cumpleanios.day)) # Resta un año si no ha cumplido años
        return edad

    def calcular_signo(self):
        cumpleanios = datetime.strptime(self.fecha_nacimiento, '%Y-%m-%d')
        zodiaco_chino = [
            {'animal': 'Mono', 'imagen': 'mono.png'}, 
            {'animal':'Gallo', 'imagen':'gallo.png'},
            {'animal':'Perro', 'imagen':'perro.png'},
            {'animal':'Cerdo', 'imagen':'cerdo.png'},
            {'animal':'Rata', 'imagen':'rata.png'},
            {'animal':'Buey', 'imagen':'buey.png'},
            {'animal':'Tigre', 'imagen':'tigre.png'},
            {'animal':'Conejo', 'imagen':'conejo.png'},
            {'animal':'Dragón', 'imagen':'dragon.png'},
            {'animal':'Serpiente', 'imagen':'serpiente.png'},
            {'animal':'Caballo', 'imagen':'caballo.png'},
            {'animal':'Cabra', 'imagen':'cabra.png'}
        ]
        return zodiaco_chino[cumpleanios.year % 12] # El año 0 es el Mono y el año 11 es la Cabra