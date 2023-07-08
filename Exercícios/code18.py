"""
Faça um programa com uma função chamada somaImposto.
A função possui dois parâmetros formais: taxaImposto,
que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
que é o custo de um item antes do imposto.
 A função “altera” o valor de custo para incluir o imposto sobre vendas.

"""

def soma_imposto(valor,imposto):
    print(f"valor do item antes do imposto: {valor}")
    print(f"Porcentagem de imposto: {imposto} %")
    com_imposto = (valor * imposto) / 100 + valor
    return f'valor do item com imposto {com_imposto}'

inss = soma_imposto(valor=1000,imposto=8)                
print(inss)
print()

preco_do_arroz = soma_imposto(imposto=25.5,valor=10)
print(preco_do_arroz)