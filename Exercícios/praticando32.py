# Criando a classe OnePuchMan

class OnePuchMan:
    def __init__(self,personagem,forca,classe):
        self.__personagem = personagem
        self.__forca = forca
        self.__classe = classe

    def get_personagem(self):
        return self.__personagem
    

    def get_forca(self):
        return f'a força do {self.__personagem} é {self.__forca}'

    def set_classe(self,ranking):
        print(f'Ranking: {ranking} da classe {self.__classe}')


class Heroi(OnePuchMan):
    tipo_personagem = 'Heroi'
    def __init__(self, personagem, forca, classe):
        super().__init__(personagem, forca, classe)

    def lutar(self,personagem):
        print(f'{personagem} está lutando..!')


saitama = Heroi('Saitama','Infinita','C')
print(saitama.get_forca())
print(saitama.get_personagem())
saitama.set_classe('B')
saitama.lutar('Saitama')

class Vilao(OnePuchMan):
    tipo_personagem = 'Vilão'
    def __init__(self, personagem, forca, classe):
        super().__init__(personagem, forca, classe)

    def lutar(self,personagem):
        print(f'{personagem} está lutando..!')

print()
garou = Vilao('Garou','Nivel God','S')
print(garou.get_personagem())
print(garou.get_forca())
garou.set_classe('Infinity')
garou.lutar('Garou')