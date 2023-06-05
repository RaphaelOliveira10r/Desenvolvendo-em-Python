# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

salario = input('Digite o valor da hora de trabalho:')
horas = input("Digite o número de horas trabalhas no mês:")
s1 = float(salario)
h1 = float(horas)

total = s1*h1
print(f"Valor total do salário mensal:{total}")