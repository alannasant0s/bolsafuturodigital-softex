def MontaSaida(*valores, separador = ", "):
    saida = separador.join(valores)
    return saida


a = MontaSaida("a","b","alanna","d")
print(a)

