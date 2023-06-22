# classe Pessoa com Módulo datetime
import datetime

total = datetime.datetime.now()


class Pessoa:
    ano_atual = total.year

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def get_nascimento(self):
        return Pessoa.ano_atual - self.idade
    

p1 = Pessoa('Maria',34)
print(p1.get_nascimento())

p2 = Pessoa('Luiza',25)
print(p2.get_nascimento())

print(Pessoa.ano_atual)