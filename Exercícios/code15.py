class Animal:
    def __init__(self,nome):
        self._nome = nome

    def cumprimentar(self):
        return f'Eu sou {self._nome}'
    

class Terrestre(Animal):
    def __init__(self, nome):
        super().__init__(nome)
    
    def andar(self):
        return f'{self._nome} andando'
    
    def cumprimentar(self):
        return f'sou {self._nome} da terra'


class Aquatico(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self._nome} nadando' 

    def cumprimentar(self):
        return f'sou {self._nome} da água' 

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