# Criando a classe OnePuchMan

class OnePuchMan:
    def __init__(self,personagem,forca,classe,organizacao):
        self.__personagem = personagem
        self.__forca = forca
        self.__classe = classe
        self.__organizacao = organizacao

    def get_personagem(self):
        return self.__personagem
    
    def organizacao(self):
        return self.__organizacao

    def get_forca(self):
        return f'a força do {self.__personagem} é {self.__forca}'

    def set_classe(self,ranking):
        print(f'Ranking: {ranking} da classe {self.__classe}')


class Heroi(OnePuchMan):
    tipo_personagem = 'Heroi'
    def __init__(self, personagem, forca, classe,organizacao):
        super().__init__(personagem, forca, classe,organizacao)


    def lutar(self,personagem):
        print(f'{personagem} está lutando..!')


saitama = Heroi('Saitama','Infinita','C','Associação de Herois')
print(saitama.get_forca())
print(saitama.get_personagem())
saitama.set_classe('B')
saitama.lutar('Saitama')
print(saitama.organizacao())


class Vilao(OnePuchMan):
    tipo_personagem = 'Vilão'
    def __init__(self, personagem, forca, classe,organizacao):
        super().__init__(personagem, forca, classe,organizacao)

    def lutar(self,personagem):
        print(f'{personagem} está lutando..!')



class Monstro(OnePuchMan):
    def __init__(self, personagem, forca, classe,organizacao):
        super().__init__(personagem, forca, classe,organizacao)


    def lutar(self,personagem):
        print(f'{personagem} está lutando..!')

  
