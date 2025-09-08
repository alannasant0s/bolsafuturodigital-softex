print("""|LISTA DE COMPRAS|
Você pode adicionar até 5 itens. """)
minha_lista = []


def lista_de_compras(lista):
    while len(lista) < 5:
        novo_item = input("Insira o ítem: ")
        lista.append(novo_item)
        print(f"O ítem {novo_item} foi inserido")

    print("\nSua lista de compras está cheia!")
lista_de_compras(minha_lista)
print("\nItens na sua lista:")
print(minha_lista)
print(f"\nEsse é o meu 2º item da lista: {minha_lista[1]}")
print(f"\nEsse é o meu 3º item da lista: {minha_lista[2]}")
