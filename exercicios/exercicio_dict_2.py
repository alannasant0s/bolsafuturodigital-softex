produtos = {}
print("Leitura dos dados")	
while True:
    cod = input("Digite o código: ")
    if cod =="":
        break
    if cod in produtos:
        print(f"Erro, o código já está cadastrado. Insira um produto diferente.")
        continue

    preco = float(input("Insira o valor do produto: "))
    produtos[cod] = preco
    
print("Fim da leitura")

for cod, preco in produtos.items(): 
    print(f"Produto {cod} custa R$ {preco:.2f}")

print("\nFim do programa")