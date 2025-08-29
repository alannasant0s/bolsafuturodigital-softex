def contar_palavras(frase):
    frase = input("Insira a sua frase: ")
    # Converte para minúsculas e remove pontuações para evitar contagem errada de caracteres
    frase_limpa = frase.lower().replace(',', '').replace('.', '') ## O replace substitui o primeiro arg pelo segundo. Ou seja, aqui ele "limpa e tira ponto e virgula"
