import random

print("""Bem vindo ao Jogo do Bicho 🐊 🦓 🐎
Aqui todos os seus sonhos são valorizados!""")

lista_bicho = ["Avetruz: 1", "Águia 2", "Burro 3", "Borboleta 4","Cachorro 5","Cabra 6","Carneiro 7","Camelo 8","Cobra 9","Coelho 10","Cavalo 11","Elefante 12","Galo 13","Gato 14","Jacaré 15","Leão 16","Macaco 17","Porco 18","Pavão 19","Peru 20","Touro 21","Tigre 22","Urso 23","Veado 24","Vaca 25"]
bicho_escolhido = int(input("Escolha um bicho de 1 a 25: "))
bicho_sorteado = random.choice(lista_bicho)
tentativas = 0

while bicho_sorteado != bicho_escolhido and tentativas < 5:
    tentativas += 1
    print("Você errou, tente novamente.")
    if bicho_sorteado == bicho_escolhido:
        print("Parabéns, você é o cara")
        break
print(f"O bicho sorteado era: {bicho_sorteado}")