class SaldoInsuficienteError(Exception):
    pass
    
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def __str__(self):
        cadena = "Cuenta de " + self.titular + " - Saldo: $" + str(self.saldo)
        return cadena
        
    def depositar(self, monto):
        self.saldo += monto
        
    def retirar(self, monto):
        if monto > self.saldo:
            raise SaldoInsuficienteError ("Algo salio mal")
        else: 
            self.saldo -= monto
        
cuenta = CuentaBancaria("Ana", 100)
cuenta.retirar(150)
print(cuenta)