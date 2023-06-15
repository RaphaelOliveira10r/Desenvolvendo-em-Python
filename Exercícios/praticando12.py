"""Faça um programa que pergunte o preço de três produtos e 
   informe qual produto você deve comprar,
   sabendo que a decisão é sempre pelo mais barato"""

# com função filter

produtos = [
    {'produto':'arroz','preco':8.99},
    {'produto':'feijão','preco':7.99},
    {'produto':'farinha','preco':2.99}
]


menor_preco = filter(lambda x: x['preco'] < 3.0,produtos)

print(f"o produto de menor valor é : {list(menor_preco)}")

