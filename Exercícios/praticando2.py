# Funções 


def equacao(x,y,z):
    return x + y * z ** 4

def decorador(funcao):
    return funcao



equacao1 = decorador(equacao(x=2,y=4,z=6))
equacao2 = decorador(equacao(y=10,z=4,x=7))
print(equacao1)
print(equacao2)