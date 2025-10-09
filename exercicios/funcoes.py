from random import randint 

def CarregarLista():
    L =[]
    for i in range(10):
        L.append(randint(1, 1000))
    return L

print("---Inicio do programa---")
valores = CarregarLista()
print(f"---Lista Gerada---{valores}")



