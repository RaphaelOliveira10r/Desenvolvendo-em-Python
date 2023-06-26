"""
Faça um programa que leia um nome de usuário e a sua senha 
e não aceite a senha igual ao nome do usuário mostrando 
uma mensagem de erro e voltando a pedir as informações. 
"""
usuario = input('digite o seu nome:')
senha = input('digite sua senha:')

if usuario == senha:
    print('digite uma senha diferente!')
else:
    print('acesso liberado!')