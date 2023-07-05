"""
Faça um programa, com uma função que necessite de três argumentos,
 e que forneça a soma desses três argumentos.
"""

def soma(x,y,z):
    soma = x+y+z
    return f'Total:{soma}'


s1 = soma(y=10,x=20,z=30)
s2 = soma(2,4,6)

print(s1)
print(s2)