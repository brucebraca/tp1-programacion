from CuentaBancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, numero, saldo_inicial=0, limite_descubierto=2000):
        # TODO: llamar a super().__init__(...) y guardar limite_descubierto
        super().__init__(titular, numero, saldo_inicial)
        self.limite_descubierto = limite_descubierto

    def extraer(self, monto):
        # TODO: validar monto > 0 y permitir saldo negativo hasta -limite_descubierto
        if monto > 0 and (self._saldo - monto) >= -self.limite_descubierto:
            self._saldo -= monto
        else:  
            raise ValueError("Monto inválido o límite de descubierto excedido.")
