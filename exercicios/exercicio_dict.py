produtos = {}
print("Leitura dos dados")	
cod = input("Digite o código: ")
while cod != "":
    preco = float(input("Insira o valor do produto"))
    produtos[cod] = preco
    cod = input("Digite o código: ")

print("Fim da leitura")
print("Preço dos produtos")
for cod in produtos.keys():
    print(f"Produto {cod} custa R$ {preco}")
print("\nFim do programa")