class CuentaBancaria:
    def __init__(self, titular, numero, saldo_inicial=0):
        self.titular = titular
        self.numero = numero
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, monto):
        # TODO: validar que monto > 0 y sumarlo al saldo
        if monto > 0:
            self._saldo += monto  

    def extraer(self, monto):
        # TODO: validar que monto > 0 y que haya saldo suficiente, y restarlo
        if monto > 0 and monto <= self._saldo:
            self._saldo -= monto
        else:
            raise ValueError("Monto inválido o saldo insuficiente.")

    def __str__(self):
        # TODO: devolver un texto descriptivo de la cuenta
        return f"Cuenta Bancaria de {self.titular}, Número: {self.numero}, Saldo: {self._saldo}"




