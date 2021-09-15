class Conta:
    banco = "Banco Qualquer Coisa"

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("===========================================")
        print(f"Banco: {Conta.banco}")
        print(f"Número: {self.__numero}")
        print(f"Titular: {self.__titular}")
        print(f"Saldo: {self.__saldo:.2f}")
        print("===========================================")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if(self.saldo - valor < -self.limite):
            print('Não é possível sacar abaixo do limite')
            return

        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
