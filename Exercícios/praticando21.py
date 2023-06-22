"""Faça um programa para a leitura de duas notas parciais de um aluno.
 O programa deve calcular a média alcançada por aluno e apresentar:
 A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 A mensagem "Reprovado", se a média for menor do que sete;
 A mensagem "Aprovado com Distinção", se a média for igual a dez."""

import statistics

lista = []
primeira = float(input("Digite as notas:"))
segunda = float(input("Digite as notas:"))

lista.append(primeira)
lista.append(segunda)

media = statistics.mean(lista)
#7media = sum(lista) / 2



if media >= 7:
    print(f"A média do aluno foi de {media} , Aprovado")
elif media < 7:
    print(f"A média do aluno foi de {media} , Reprovado")
else:
    print('Aprovado com Distinção')



