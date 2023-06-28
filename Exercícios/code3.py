# Exercitando Json e Leituras de arquivos :
import json




produtos =[
    {'produto':'Geladeira','preço':2500},
    {'produto':'Fogão','preço':900},
    {'produto':'Armário','preço':500},
    {'produto':'Cafeteira','preço':120},
    {'produto':'Liquidificador','preço':120},
    {'produto':'Notebook','preço':1200},
    {'produto':'Garrafa de café','preço':50},
    {'produto':'Balcão de cozinha','preço':220},
    {'produto':'Tv','preço':1500},
    {'produto':'Cama','preço':1350},
    {'produto':'Utensílios de cozinha','preço':150},
    {'produto':'Potes de matimentos','preço':80},
    {'produto':'xicaras','preço':45},
    {'produto':'Copos','preço':60}
    
    ]


with open('arquivo.json','w',encoding='utf8') as arquivo:
        json.dump(produtos,arquivo,ensure_ascii=False,indent=2)

