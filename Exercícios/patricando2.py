# Funções 


def equacao_1_grau(x,y,z):
    return x + y * z ** 4

def decorador(funcao):
    return funcao



equacao = decorador(equacao_1_grau(2,4,6))
print(equacao)