alunos = []
print("Bem vindo ao Cadastro de Alunos")

while True:
    nome = input("Insira seu nome: ")
    email = input("Insira seu email: ")

    aluno_dicionario = {
    "nome": nome,
    "email": email
}    

    alunos.append(aluno_dicionario)
    print(f"O aluno {nome} foi cadastrado com sucesso")

    continuar = input("Deseja cadastrar outro aluno? (s/n): ")
    if continuar.lower != 's':
         break
if not alunos: 
    print("Nenhum aluno foi cadastrado.")
else:   
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Email: {aluno['email']}")    

