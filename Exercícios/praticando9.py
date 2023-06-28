# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

# altura = float(input("Digite a sua altura em metros: "))
# peso = (72.7 * altura) - 58
# print(f"Seu peso ideal é: {peso}")

def peso_ideal(altura=float):
    peso = (72.7 * altura) - 58
    return f"Seu peso ideal é: {peso}"

print(peso_ideal(altura=1.85))