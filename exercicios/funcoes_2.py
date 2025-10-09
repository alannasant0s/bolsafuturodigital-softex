from random import randint 

def CarregarLista(qtde):
    L =[]
    for i in range(qtde):
        L.append(randint(1, 1000))
    return L

q = int(input("Insira a quantidade de números a ser gerados: "))

valores = CarregarLista(q)
print(f"Os números gerados foram: {valores}")