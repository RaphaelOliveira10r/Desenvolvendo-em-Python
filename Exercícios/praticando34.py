class Pessoa:
    def __init__(self,nome,sobrenome,cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def get_identificacao(self):
        return f'{self.__cpf}'
    

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome, cpf,codigo):
        super().__init__(nome, sobrenome, cpf,codigo)
        self.__codigo = codigo

    def get_identificacao(self):
        return f'{self.__codigo}'
    

class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf,matricula):
        super().__init__(nome, sobrenome, cpf,matricula)
        self.__matricula = matricula
    
    def get_identificacao(self):
        return f'{self.__matricula}'