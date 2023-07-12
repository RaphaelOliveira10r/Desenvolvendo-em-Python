

def area_circulo(raio):
    PI = 3.14           # CONSTANTE
    area = PI * (raio **2)
    return area

raio = float(input("Digite o valor do raio:"))

a1 = area_circulo(raio=raio)
print(a1)