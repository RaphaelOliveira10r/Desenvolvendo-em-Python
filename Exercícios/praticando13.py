# mapeando lista com dic

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


mapeando_precos = map (lambda x:x['preço'],exemplo)
print(list(mapeando_precos))