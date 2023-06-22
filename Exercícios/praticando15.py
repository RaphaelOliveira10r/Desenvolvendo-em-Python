# Criando uma classe Notebook

class Notebook:
    def __init__(self,nome,ligado=False,desligado=False):
        self.__nome = nome
        self.__ligado = ligado
        self.__desligado = desligado

    def ligar(self):
        if self.__ligado:
            print(f"{self.__nome} já está ligado")
            return
        self.__ligado = True
        print(f"{self.__nome} está ligado")


    def desligar(self):
        if self.__desligado:
            print(f'O notebook {self.__nome} já está desligado.')
            return
        self.__desligado = True
        print(f"{self.__nome} está desligado")

    def reiniciar(self):
        print(f'{self.__nome} está reiniciando')


    def suspender(self):
        print(f"{self.__nome} está suspenso")



note1 = Notebook('Dell')


# se o método for chamado uma segunda vez,
# irá retorna que o notebook já está ligado
# ou desligado


note1.ligar()
note1.ligar()
note1.desligar()
note1.desligar()
note1.reiniciar()
note1.suspender()
