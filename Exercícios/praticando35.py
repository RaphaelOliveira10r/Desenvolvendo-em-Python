
class Celular:
    def __init__(self,nome,marca,capacidade,camera):
        self._nome = nome
        self._marca = marca
        self._capacidade = capacidade
        self._camera = camera

    def get_nome_marca(self):
        print(f'O celular {self._nome} da marca {self._marca}')

    def get_capacidade(self):
        print(f"Com {self._capacidade} GB de armazenamento interno.")

    def get_camera(self):
        print(f'Resolução da câmera: {self._camera} MP')
    
    def ligar(self):
        return f'Está ligado.'

    def desligar(self):
        return f'Está desligado.'
    
    def carregar(self):
        return f'Está carregando...'
    
     
    
    
samsung = Celular("Galaxy A52","Samsung",128,52)
samsung.get_nome_marca()
samsung.get_capacidade()
samsung.get_camera()
print(samsung.carregar())
print(samsung.desligar())
print(samsung.ligar())