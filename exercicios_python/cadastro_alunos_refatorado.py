alunos = []

# Criando a função do menu inicial
def inicio_menu():
    print("""================================
|Bem vindo ao Cadastro de Alunos|          
================================""")

# Criando a função que solicita dados
def solicitar_dados():
    nome = input("Insira seu nome: ")
    email = input("Insira seu email: ")
    aluno_dicionario = {
    "nome": nome,
    "email": email
}    
    alunos.append(aluno_dicionario)
    print(f"O aluno {nome} foi cadastrado com sucesso")

#Criando a função de continuar
def funcao_continuar():
    continuar = int(input("Deseja cadastrar outro aluno? Digite 1 para sim/ 2 para sair: "))
    if continuar == 1:
            return solicitar_dados()
    elif continuar == 2:
            print("Fim do programa")
    else: 
            print("Nenhuma ação realizada, insira uma entrada válida.")   



inicio_menu()
solicitar_dados()
funcao_continuar()
