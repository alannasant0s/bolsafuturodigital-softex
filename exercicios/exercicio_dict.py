produtos = {}
print("Leitura dos dados")	
cod = input("Digite o código: ")
while cod != "":
    preco = float(input("Insira o valor do produto"))
    produtos[cod] = preco
    cod = input("Digite o código: ")

print("Fim da leitura")