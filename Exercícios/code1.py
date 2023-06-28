# Treinando Funções
def reverter_string(string,valor_aleatorio):
     print(string,valor_aleatorio)
     return string[::-1],valor_aleatorio[::-1]

nome = reverter_string(valor_aleatorio='Coder',string='Raphael')
print(nome)
print(type(nome))