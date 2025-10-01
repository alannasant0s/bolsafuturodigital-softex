class Apostador:
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo = float(saldo_inicial)

    def depositar(self, valor):
        self.saldo += valor
        print(f"{self.nome} depositou R${valor:.2f}. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"{self.nome} sacou R${valor:.2f}. Saldo restante: R${self.saldo:.2f}")
        else:
            print(f"{self.nome} tentou sacar R${valor:.2f}, mas o saldo é insuficiente.")

jogador1 = Apostador("Alanna", 500.00)
jogador2 = Apostador("Áurea", 100.00)

print(f"Estado Inicial: {jogador1.nome} tem R${jogador1.saldo:.2f}, {jogador2.nome} tem R${jogador2.saldo:.2f}")
print("-" * 30)

jogador1.depositar(200.00)

jogador2.sacar(150.00)

jogador2.depositar(50.00)

jogador2.sacar(150.00)

print("-" * 30)
print(f"Estado Final: {jogador1.nome} tem R${jogador1.saldo:.2f}, {jogador2.nome} tem R${jogador2.saldo:.2f}")