# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# o salário bruto.
# o quanto pagou ao INSS.
# o quanto pagou ao sindicato.
# o o salário líquido.
# o calcule os descontos e o salário líquido, conforme a tabela abaixo:

hora = float(input("Digite o valor de cada hora de trabalho: "))
n_horas = float(input('Digite o número de horas trabalhadas no mês: '))
salario_bruto = hora * n_horas


imposto_de_renda = 11
inss = 8
sindicato = 5

pago_imposto_renda = (salario_bruto * imposto_de_renda) / 100
pago_inss = (salario_bruto * inss) / 100
pago_sindicato = (salario_bruto * sindicato)/100

total_descontado = (pago_imposto_renda + pago_inss) + pago_sindicato

salario_liquido = salario_bruto - total_descontado

print(f'O salario bruto do mês: {salario_bruto}')
print()
print('---------DESCONTOS-----------------')

print(f"Valor pago ao Inss : {pago_inss}")
print(f"Valor pago ao imposto de renda: {pago_imposto_renda}")
print(f"Valor pago ao sindicato: {pago_sindicato}")
print(f'Total de descontos: {total_descontado}')
print('-----------------------------------')
print(f"Salário líquido: {salario_liquido}")





