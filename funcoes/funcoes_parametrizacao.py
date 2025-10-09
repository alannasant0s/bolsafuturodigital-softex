from random import randint 

def CarregarLista(qtde, a , b):
    """Carrega uma lista com qtde elementos inteiros aleatórios entre a e b"""
    L =[]
    for i in range(qtde):
        L.append(randint(a, b))
    return L

q = int(input("Insira a quantidade de números a ser gerados: "))
lmin = int(input("Insira o limite mínimo: "))
lmax = int(input("Insira o limite máximo: "))
valores = CarregarLista(q, lmin, lmax)


print(f"Os números gerados foram: {valores}")
print(f"Foram gerados {q} valores. Onde o limite mínimo foi o {lmin} e o limite máximo foi o {lmax}")