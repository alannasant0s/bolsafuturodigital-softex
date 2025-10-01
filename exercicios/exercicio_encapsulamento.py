class ContaBancaria:
 def __init__(self, saldo_inicial):
 # Atributo 'privado' (protegido por convenção)
    self.__saldo = saldo_inicial

 # Método (Getter) para acessar o saldo
 def consultar_saldo(self):
    return f"Saldo atual: R$ {self.__saldo:.2f}"

 # Método (Setter) para depositar (alterar o saldo)
 def depositar(self, valor):
    if valor > 0:
        self.__saldo += valor
        return f"Depósito de R$ {valor:.2f} realizado."
    return f"Valor de depósito inválido."
# Objeto
minha_conta = ContaBancaria(saldo_inicial=500)
# Ação
print("--- Encapsulamento ---")
print(minha_conta.consultar_saldo())
print(minha_conta.depositar(150))
# Tentar alterar o saldo diretamente (o encapsulamento impede ou desincentiva isso)
minha_conta.__saldo = 10000000
print(minha_conta.consultar_saldo())