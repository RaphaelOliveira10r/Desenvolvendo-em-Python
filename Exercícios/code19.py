"""
Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721.
"""
def num_revers(num):
    numero = []
    num = str(num)
    for i in range(len(num)-1,-1,-1):
        numero.append(num[i])
    return int("".join(numero))


print(num_revers(1234))