

class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("===========================================")
        print(f"Número: {self.__numero}")
        print(f"Titular: {self.__titular}")
        print(f"Saldo: {self.__saldo:.2f}")
        print("===========================================")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
