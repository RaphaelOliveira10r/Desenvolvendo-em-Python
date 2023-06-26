# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue 
# pedindo até que o usuário informe um valor válido. 


nota = 0
while nota !=6:
    nota = int(input('Digite uma nota de 0 a 10:'))
    print('valor inválido')
    if nota == 6:
        print('valor válido')
        break
    