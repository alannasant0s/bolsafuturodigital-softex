import random

contador = 0
comodos_da_casa = ["Armário","Geladeira","Caixa de Sapato","Fogão","Guarda Roupa","Banheiro","Cola Rato","Ratoeira"]
encontrou = False
resposta = random.randint(1,8)

while contador < 5:
    palpite_usuario = int(input("""|=============================|
|  JOGO CAÇA AO QUEIJO 🐁🧀   |
|=============================|
ONDE O QUEIJO ESTÁ? Selecione a opção:
[1] Armário
[2] Geladeira
[3] Caixa de Sapato
[4] Fogão
[5] Guarda Roupa
[6] Banheiro
[7] Cola Rato
[8] Ratoeira        
Você tem 5 chances...   
DIGITE O NÚMERO CORRESPONDENTE: """))

    if palpite_usuario == resposta:
        print("PARABÉNS, O RATO ENCONTROU O QUEIJO.🧀")
        encontrou = True
        break
    
    else:   
        print(f"Você errou, o queijo não está aqui. Tente novamente.")
    contador +=1
    
if not encontrou:
        print("Lamento, suas tentativas acabaram!")

resposta_correta = comodos_da_casa[resposta - 1]
print(f"O local onde o queijo estava é na(o) {resposta} ({resposta_correta})")