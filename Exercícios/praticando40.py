


def area_cilindro(raio,altura):

    def area_circulo(raio): # está função só será reconhecida dentro deste escopo
        PI = 3.141592
        area = PI *(raio**2)
        return area
    
    area = area_circulo(raio) * altura
    return area


raio = float(input("Digite o valor do raio do cilindro:"))
altura = float(input("Digite a altura do cilindro:"))

a = area_cilindro(raio=raio,altura=altura)
print(f'area do cilindro:{a}')
print('-------------')

