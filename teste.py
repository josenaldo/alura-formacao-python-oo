def cria_conta(numero, titular, saldo, limite):
    conta = {
        'numero': numero,
        'titular': titular,
        'saldo': saldo,
        'limite': limite,
    }

    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print("===========================================")
    print(f"Número: {conta['numero']}")
    print(f"Titular: {conta['titular']}")
    print(f"Saldo: {conta['saldo']:.2f}")
    print("===========================================")
