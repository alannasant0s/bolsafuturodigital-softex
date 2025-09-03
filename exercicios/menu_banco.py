def saudacao_personalizada(usuario):
    print(f"Seja bem vindo(a) {usuario}, selecione a operação que deseja realizar:")


def menu_banco():
    print("""|==============================| 
|     BANCO NOSSO DINHEIRO     |
|==============================|                  
|     1 - Ver Saldo            |
|     2 - Realizar Depósito    |
|     3 - Realizar Saque       |
|     4 - Sair                 |
|==============================|""")

usuario = input("Qual o seu nome? ")
saudacao_personalizada(usuario)
menu_banco()
