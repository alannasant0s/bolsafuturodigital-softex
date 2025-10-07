Lst = []


for linha in open("entrada_er.txt", "r"):
    Lst.append(int(linha))

print("Lista de arquivos")
print(Lst)

Soma = sum(Lst)
print(f" A soma dos valores é {Soma}.")

Qtde = len(Lst)
Media = Soma / Qtde
print(f"A média dos valores é: {Media}")