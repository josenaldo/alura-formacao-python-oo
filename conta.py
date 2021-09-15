

class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("===========================================")
        print(f"Número: {self.numero}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: {self.saldo:.2f}")
        print("===========================================")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
