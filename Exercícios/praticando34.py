# Praticando classe com polimofirmo na identificação
class Pessoa:
    def __init__(self,nome,sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def identificacao(self):
        return self.__cpf
    


class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf,codigo):
        super().__init__(nome, sobrenome, cpf)
        self.__codigo = codigo

    def identificacao(self):
        return self.__codigo
    


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf,matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula
    
    def identificacao(self):
        return self.__matricula
    

c1 = Cliente("Maria","Silva","451236789010","1234-5")
print(c1.nome_completo())
print(c1.identificacao())

print()
f1 = Funcionario("José","Lopes","069873215412","5462-9")

print(f1.nome_completo())
print(f1.identificacao())