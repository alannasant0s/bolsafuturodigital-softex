selecao = int(input("""============================
| Seja bem vindo a sua calculadora |
| Selecione a operação a realizar  |
|==================================|
|        1 - Somar               |
|        2 - Subtrair            |
|        3 - Multiplicar         |
|        4 - Dividir             |
|==================================|
"""))

if selecao >= 1 and selecao <= 4:
    numero1 = int(input("Insira o primeiro número: "))
    numero2 = int(input("Insira o segundo número: "))

    if selecao == 1:
        soma = numero1 + numero2
        print(f"A soma de {numero1} + {numero2} é: {soma}")
        
    elif selecao == 2:
        if numero1 < numero2:
            print("O primeiro número deve ser maior que o segundo.")
        subtracao = numero1 - numero2
        print(f"A subtração de {numero1} - {numero2} é: {subtracao}")
        
    elif selecao == 3:
        multiplicacao = numero1 * numero2
        print(f"A multiplicação de {numero1} * {numero2} é: {multiplicacao}")
        
    elif selecao == 4:
        if numero1 < numero2:
            print("O primeiro número deve ser maior que o segundo.")
        if numero2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            divisao = numero1 / numero2
            print(f"A divisão de {numero1} / {numero2} é: {divisao}")

else:
    print("Insira uma opção válida")