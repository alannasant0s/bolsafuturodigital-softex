n = 1
while n != 0:
    n = int(input("Digite um número inteiro"))
    match n:
        case 1:
            print("Você digitou um: ")
        case 2:
            print("Você digitou dois: ")
        case 3:
            print("Você digitou três: ")
        case _:
            print("Você digitou outra coisa.")
        
    print("Fim do programa")