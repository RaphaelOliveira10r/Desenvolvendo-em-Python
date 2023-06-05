# Funções 


def equacao(x,y,z):
    return x + y * z ** 4

def decorador(funcao):
    return funcao



equacao = decorador(equacao(2,4,6))
print(equacao)