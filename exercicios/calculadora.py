print("""Selecione o tipo de operação que deseja efetuar:
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão""")
calculadora = float(input("Selecione o tipo de operação que deseja efetuar: "))

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

if calculadora == 1 :
    print(f"O resultado da soma dos números é: {soma}")
elif calculadora == 2 :
    print(f"O resultado da subtração dos números é: {subtracao}")
elif calculadora == 3 :
    print(f"O resultado da divisão dos números é: {multiplicacao}")
elif calculadora == 4 :
    print(f"O resultado da multiplicação dos números é: {divisao}")
else:
    print("Insira uma opção válida")