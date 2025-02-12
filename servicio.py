class Servicio:
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