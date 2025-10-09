Lst = []


for linha in open("entrada_er.txt", "r"):
    Lst.append(int(linha))

print("Lista de arquivos")
print(Lst)

Qtde = len(Lst)
print(f"Quantidade: {Qtde}")

Soma = sum(Lst)
print(f" A soma dos valores é: {Soma}.")
print(f"A média dos valores é: {Soma / Qtde}")