
class Exercito:
    def __init__(self,pais,ranking,quantidade):
        self._pais = pais
        self._ranking = ranking
        self._quantidade = quantidade

    def get_pais(self):
        return f'País: {self._pais}'
    
    def get_ranking(self):
        return f'Ranking: {self._ranking}'
    
    def get_quantidade(self):
        return f'Contingente: {self._quantidade} mil soldados ativos!'
    

brasil = Exercito("Brasil",10,200)
print(brasil.get_pais())
print(brasil.get_ranking())
print(brasil.get_quantidade())