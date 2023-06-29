class Animal:
    def __init__(self,nome):
        self.__nome = nome

    def emite_som(self):
        pass


class Arara(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emite_som(self):
        print('Grasna')


class Cascavel(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def emite_som(self):
        print('Chacoalha')


cobra = Cascavel('Python')
cobra.emite_som()
ave = Arara('Papagaio')
ave.emite_som()