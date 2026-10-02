from cuenta_bancaria import CuentaBancaria
from cuenta_corriente import CuentaCorriente
from caja_de_ahorro import CajaDeAhorro
    

class Banco:
    def __init__(self, nombre):
        # TODO
        self.nombre = nombre
        self._cuentas = {}

    def agregar_cuenta(self, cuenta):
        # TODO
        if cuenta.numero in self._cuentas:
            raise ValueError("La cuenta ya existe en el banco.")
        self._cuentas[cuenta.numero] = cuenta

    def buscar_cuenta(self, numero):
        # TODO
        return self._cuentas.get(numero, None)

    def transferir(self, numero_origen, numero_destino, monto):
        # TODO
        cuenta_origen = self.buscar_cuenta(numero_origen)
        cuenta_destino = self.buscar_cuenta(numero_destino)
        if cuenta_origen is None or cuenta_destino is None:
            raise ValueError("Una o ambas cuentas no existen.")
        cuenta_origen.extraer(monto)
        cuenta_destino.depositar(monto)

    def total_depositado(self):
        # TODO
        total  = sum(cuenta.saldo for cuenta in self._cuentas.values())
        return total    

    def listar_cuentas(self):
        # TODO
        for cuenta in self._cuentas.values():
            print(cuenta)



