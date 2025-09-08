nome = input("Olá, qual o seu nome? ")
palavra = input("Digite uma palavra: ")

maiuscula = palavra.upper()
minuscula = palavra.lower()
contagem_silabas = len(palavra)

print(f"Olá {nome}")
print(f"A frase em maíuscula fica assim: {maiuscula}")
print(f"A frase em minuscula fica assim: {minuscula}")
print(f"Essa palavra possui {contagem_silabas} sílabas")