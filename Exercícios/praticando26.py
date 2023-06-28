lista = [
    {'nome':'Claúdia','idade':38},
    {'nome':'Raphael','idade':24},
    {'nome':'Sarah','idade':33},
    {'nome':'Marcela','idade':19},
    {'nome':'Guilherme','idade':27},
    {'nome':'Ana Carla','idade':27},
    {'nome':'Marina','idade':18},
    {'nome':'Paula','idade':35},
         ]
mapeando = list(map(lambda x:x['idade'],lista))
print(mapeando)