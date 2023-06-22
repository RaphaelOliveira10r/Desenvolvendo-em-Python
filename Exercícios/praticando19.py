# Treinamento de class

class Pessoa:
    def __init__(self,nome,idade,cidade):
        self.__nome = nome
        self.__idade = idade
        self.__cidade = cidade

    def __str__(self):
        return self.__cidade
    
    def get_idade(self):
        print(f"{self.__nome} tem {self.__idade} de idade.")
        

    def get_nome(self):
        return self.__nome

    def set_nome(self,novo):
        self.__nome = novo
        print(f"O nome foi alterado para {novo}")


eu = Pessoa('Ralph',24,'Brasília')

print(eu.get_nome())
eu.set_nome('Raphael')




