import random

def jogo_advinhacao():
    numero_secreto = random.randint(1, 100)
    max_tentativas = 10
    tentativas_feitas = 0

    print("--- Jogo da Advinhação Iniciado (1 a 100) ---")

    while tentativas_feitas < max_tentativas:
        palpite = int(input(f"Tentativa nº {tentativas_feitas + 1}, restam {max_tentativas - (tentativas_feitas + 1)}.Insira seu palpite: "))
        
        tentativas_feitas += 1
        
        if palpite > numero_secreto:
            print("Seu palpite foi muito alto")
        elif palpite < numero_secreto:
            print("Seu palpite foi muito baixo")
        else:
            print("Parabéns, você acertou")
            break
    if tentativas_feitas == max_tentativas and palpite != numero_secreto:
        print(f"Obrigado(a) por participar, sua chances acabaram. O número secreto era ({numero_secreto}).")   
   

jogo_advinhacao()
    