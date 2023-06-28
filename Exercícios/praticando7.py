# Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Farenheit.

def temperatura_faranheit(celsius):
    f = (celsius * 9) / 5 + 32
    return f'a temperatura de celcius para farenheit é : {f}'


print(temperatura_faranheit(celsius=17))


