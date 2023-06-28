
def calcular_imposto(preco,taxa,outro_valor=None):
    imposto = preco * taxa 
    print(preco,taxa,outro_valor)
    return imposto

print(__name__)


if __name__ == "__main__":
    print(calcular_imposto(1000,0.2))