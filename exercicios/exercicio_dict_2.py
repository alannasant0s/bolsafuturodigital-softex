produtos = {}
print("Leitura dos dados")	
cod = input("Digite o código: ")
while cod != "":
    if cod in produtos:
        print(f"Erro, o código já está cadastrado. Insira um produto diferente.")
        cod = input("Digite o código: ")
    preco = float(input("Insira o valor do produto: "))
    produtos[cod] = preco
    cod = input("Digite o código: ")
    
print("Fim da leitura")

for cod in produtos.keys(): 
    print(f"Produto {cod} custa R$ {produtos[cod]}")
print("\nFim do programa")