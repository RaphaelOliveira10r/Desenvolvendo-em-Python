# faça um programada que peça 4 notas e peça pra mostrar a média de todas 
# as notas


import statistics

notas = []
nota = 0
while True:
    nota = float(input('Digite as notas:'))
    notas.append(nota)
    if nota == 0:
        
        break

notas.pop()

def estatistica_notas(lista):
    media = statistics.mean(lista)
    print(f'Média de todas as notas : {media}')
    return media

estatistica_notas(lista=notas)
print(f'Notas : {notas}')
