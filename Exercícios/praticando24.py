class Carro:
    def __init__(self,nome,placa,ano,velocidade):
        self.nome = nome
        self.placa = placa
        self.ano = ano
        self.velocidade = velocidade

    def get_nome(self):
        return self.nome
    
    def get_placa(self):
        return self.placa
    
    def get_ano(self):
        print(f'Ano de fabricação do {self.nome}: {self.ano}')

    def velocidade_atual(self):
        return f'{self.nome} está a uma velocidade de {self.velocidade}'


class Sedan(Carro):
    tipo = 'sedan'
    def estilo(self):
        print(f'O tipo do {self.nome} é um sedan')


corolla = Sedan(ano=2016,velocidade=134,placa='TGF7654',nome='Corolla')
print(corolla.get_nome())
print(corolla.get_placa())
corolla.get_ano()
print(corolla.tipo)
corolla.estilo()
print(corolla.velocidade_atual())
print()

class Caminhonete(Carro):
    tipo = 'Caminhonete'
    def estilo(self):
        print(f'O tipo do {self.nome} é uma caminhonete.')



hilux = Caminhonete(nome='Hilux',placa='PYT76',ano=2017,velocidade=150)
print(hilux.get_nome())
print(hilux.get_placa())
hilux.get_ano()
print(hilux.tipo)
hilux.estilo()
