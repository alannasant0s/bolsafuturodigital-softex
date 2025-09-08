
def contar_palavras(frase):
    # abaixo convertemos para minuscula e removemos pontuações para evitar contagem errada de caracteres
    frase_limpa = frase.lower().replace(',', '').replace('.', '') ## O replace substitui o primeiro arg pelo segundo. Ou seja, aqui ele "limpa e tira ponto e virgula"
    palavras = frase_limpa.split() #Separa as palavras em uma lista
    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

# Verificando os valores do resultado da contagem
    print("Lista de palavras:", palavras)
    print("Frequência de cada palavra:", frequencia)


frase = input("Insira a sua frase: ")
contar_palavras(frase)
