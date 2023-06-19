# Filtrando valor dos produtos maior que 1000


exemplo = [
    {'produto':'Geladeira','preço':1500},
    {'produto':'Fogão','preço':899},
    {'produto':'Microondas','preço':450},
    {'produto':'Televisão','preço':1200},
    {'produto':'Notebook','preço':2500},
    {'produto':'Cama','preço':1199},
    {'produto':'Mesa','preço':250},
    {'produto':'Ferro de passar','preço':80},
    {'produto':'Liquidificador','preço':120},
    {'produto':'Forno Elétrico','preço':349},
    ]


def filtrar(lista):
    return list(filter(lambda x:x['preço'] > 1000 , lista))

print(filtrar(exemplo))