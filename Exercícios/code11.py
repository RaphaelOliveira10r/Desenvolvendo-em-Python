# Herança Multipla

class Classe1:
    def __init__(self,nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


class Classe2(Classe1):
    def __init__(self, nome,endereco):
        super().__init__(nome)
        self.__endereco = endereco

    def get_endereco(self):
        return self.__endereco


class Classe3(Classe2):
    def __init__(self, nome, endereco,salario):
        super().__init__(nome, endereco)
        self.__salario = salario

    def get_salario(self):
        return self.__salario
    



pessoa = Classe3("Pedro","São Paulo","1500")

print(pessoa.get_nome())
print(pessoa.get_endereco())
print(pessoa.get_salario())