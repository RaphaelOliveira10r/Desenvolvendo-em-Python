#Faça um Programa que leia três números e mostre-os em ordem decrescente.
lista = []
while True:
    num = int(input('digite um número: '))
    lista.append(num)
    if num ==0:
        break



lista.reverse()

print(lista)

