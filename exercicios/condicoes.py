salario = float(input("Informe o valor do seu salário: "))
trabalho_clt_str = (input("Você trabalha no regime CLT? (sim/não): "))
trabalho_clt = trabalho_clt_str.lower() == 'sim'

if salario < 1500:
    print("Lamento, no momento não será possivel continuar o processo")
elif salario >= 1500 and trabalho_clt == True:
    print("Parabéns, iremos te mostrar todos os planos")
else:
    print("Seu número foi enviado para nosso banco de dados. Caso surjam oportunidades vinculadas ao seu perfil, entraremos em contato")