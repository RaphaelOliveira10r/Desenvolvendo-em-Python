class Animal:
    def __init__(self,nome):
        self.__nome = nome


    def get_nome(self):
        return self.__nome


    def cumprimentar(self):
        return f'Eu sou {self.__nome}'
    




class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'{super().get_nome()} andando'
    
    def cumprimentar(self):
        return f'sou {super().get_nome()} da terra'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{super().get_nome()} nadando' 

    def cumprimentar(self):
        return f'sou {super().get_nome()} da água' 

alex = Terrestre("Leão alex")
print(alex.andar())
print(alex.cumprimentar())    
print()

fisher = Aquatico("Peixe fisher")
print(fisher.nadar())
print(fisher.cumprimentar())
print()


class Pinguim(Terrestre,Aquatico):
    def __init__(self, nome):
        super().__init__(nome)

pinguim = Pinguim("Pinguim")
print(pinguim.cumprimentar())
print(pinguim.nadar())
print(pinguim.andar())


print(help(Pinguim)) #ao dar um help na classe Pinguim, irá imprimir a ordem de execução