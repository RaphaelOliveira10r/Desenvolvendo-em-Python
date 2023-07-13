
class Exercito:
    def __init__(self,pais,ranking,quantidade,localizacao):
        self._pais = pais
        self._ranking = ranking
        self._quantidade = quantidade
        self._localizacao = localizacao

    def get_pais(self):
        return f'País: {self._pais}'
    
    def get_ranking(self):
        return f'Ranking: {self._ranking}'
    
    def get_quantidade(self):
        return f'Contingente: {self._quantidade} mil soldados ativos!'
    

class Marinha(Exercito):
    def __init__(self, pais, ranking, quantidade, localizacao,navios):
        super().__init__(pais, ranking, quantidade, localizacao)
        self._navios = navios
    
    def get_navios(self):
        return f'Quantidade de Navios:{self._navios}'


class Aeronautica(Exercito):
    def __init__(self, pais, ranking, quantidade, localizacao,avioes):
        super().__init__(pais, ranking, quantidade, localizacao)
        self._avioes = avioes

    def get_avioes(self):
        return f'Quantidade de Aviões:{self._avioes}'
    


ebr = Marinha('Brasil',10,200,'America do Sul',134)
print(ebr.get_pais())
print(ebr.get_quantidade())
print(ebr.get_navios())
print(ebr.get_ranking())


print('-----------------------------')
eua = Aeronautica("Estados Unidos",1,350,"America do Norte",5000)
print(eua.get_pais())
print(eua.get_ranking())
print(eua.get_quantidade())
print(eua.get_avioes())
