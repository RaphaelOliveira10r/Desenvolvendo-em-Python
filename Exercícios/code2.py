"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores 
e lhe contraram para desenvolver o programa que calculará os reajustes.
o Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o o salário antes do reajuste;
o o percentual de aumento aplicado;
o o valor do aumento;
o o novo salário, após o aumento.
"""


salario = float(input("Digite o valor do salário:"))
print(f'Valor do salário sem reajuste: {salario} reais.')

if salario <= 280:
    print(f"valor do aumento do salario: {(salario *20)/100}")
    print(f"valor total do salário com o aumento: {((salario *20)/100)+ salario}")
    print(f"aumento salarial de 20%.")
elif salario > 280 and salario <= 700:
    print(f"valor do aumento do salario: {(salario *15)/100}")
    print(f"valor total do salário com o aumento: {((salario *15)/100)+ salario}")
    print(f"aumento salarial de 15%.")
elif salario > 700 and salario <= 1500:
    print(f"valor do aumento do salario: {(salario *10)/100}")
    print(f"valor total do salário com o aumento: {((salario *10)/100)+ salario}")
    print(f"aumento salarial de 10%")
else:
    print(f"valor do aumento do salario: {(salario *5)/100}")
    print(f"valor total do salário com o aumento: {((salario *5)/100)+ salario}")
    print(f"aumento salarial de 5%.")
