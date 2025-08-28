## Exercício – Cálculo de Salário com Descontos
"""1. Solicite ao usuário:
■ O valor recebido por hora trabalhada;
■ A quantidade de horas trabalhadas no mês.
2. Calcule:
■ Salário Bruto (valor da hora × horas trabalhadas);
■ Desconto do Imposto de Renda (11%);
■ Desconto do INSS (9%);
■ Desconto do Sindicato (4%);
■ Salário Líquido (Salário Bruto − soma dos descontos).
3. Apresente o resultado no seguinte formato:
● + Salário Bruto : R$ xxxx.xx
● - IR (11%) : R$ xxxx.xx
● - INSS (9%) : R$ xxxx.xx
● - Sindicato (4%) : R$ xxxx.xx
● = Salário Líquido : R$ xxxx.xx"""

hora_trabalhada = float(input("Qual o valor da hora trabalhada? "))
qtd_hrs = float(input("Quantas horas foram trabalhadas no mês? "))

salario = hora_trabalhada * qtd_hrs
percentual_ir = 0.11 
percentual_inss = 0.09 
percentual_sindicato = 0.04 

desconto_ir = salario * percentual_ir
desconto_inss = salario * percentual_inss
desconto_sindicato = salario * percentual_sindicato
descontos_totais = desconto_ir + desconto_inss + desconto_sindicato

print(f"O valor bruto do salário é R$ {salario} ")
print(f"O valor do desconto do imposto de renda é R$ {desconto_ir} ")
print(f"O valor do desconto do INSS é R$ {desconto_inss} ")
print(f"O valor do desconto do sindicato é R$ {desconto_sindicato} ")

print(f"O valor do salário com descontos é R$ {salario - descontos_totais } ")
