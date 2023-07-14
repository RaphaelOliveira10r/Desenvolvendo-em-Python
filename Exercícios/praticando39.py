import statistics


notas = [10,9,8,7,6,5,4,3,2,1]


def media_notas(lista):
    media = statistics.mean(lista)
    return  f'Média de todas as notas: {media}'


print(media_notas(notas))