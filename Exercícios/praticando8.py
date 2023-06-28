# sorteando nomes com choice

from random import choice

nomes = ['Raphael','José','João','Ana','Clara','Antonia']

def sortear_nome(lista):
     print(f'Nome sorteado: {choice(lista)}')


sortear_nome(lista=nomes)


