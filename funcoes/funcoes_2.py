from random import randint 

def CarregarLista(qtde):
    """Carrega uma lista com qtde elementos inteiros aleatórios."""
    L =[]
    for i in range(qtde):
        L.append(randint(1, 1000))
    return L

q = int(input("Insira a quantidade de números a ser gerados: "))

valores = CarregarLista(q)
print(f"Os números gerados foram: {valores}")
print(f"Foram gerados {q} valores.")