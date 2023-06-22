# faça um programa que peça a multiplicação 
# e a soma de um vetor(lista)


numeros = [10,35,67,98,102]

lc_soma = [x + 2 for x in numeros]
lc_multiplicacao = [x * 2 for x in numeros]

print('resultado da multiplicação em list comprehesion: ',lc_multiplicacao)
print('resultado da soma em list comprehesion :',lc_soma)