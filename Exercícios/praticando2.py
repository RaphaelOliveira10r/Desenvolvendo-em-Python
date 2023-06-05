# Funções 


def equacao(x,y,z):
    return x + y * z ** 4

def decorador(funcao):
    return funcao



equacao1 = decorador(equacao(2,4,6))
equacao2 = decorador(equacao(10,4,7))
print(equacao1)
print(equacao2)