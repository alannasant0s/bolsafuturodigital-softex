Precos = []
print("Forneça os preços para a lista. Zero para terminar")
preco = float(input("Insira um valor real: "))
while preco != 0:
    Precos.append(preco)
    preco = float(input("..Digite um valor real: "))
print("Os preços são esses: ")
print(Precos)


aumento = float(input("Digite a porcetantagem de aumento: "))
NovosPrecos = [valor *(1 + aumento/100) for valor in Precos]
for valor in NovosPrecos:
    print(f"{valor:.2f}")
print("Fim do programa")