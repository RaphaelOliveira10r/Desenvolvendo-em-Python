class Cidade:
    def __init__(self,nome,estado,regiao):
        self.nome = nome
        self.estado = estado
        self.regiao = regiao

    def get_nome(self):
        return self.nome
    

city1 = Cidade('Recanto das Emas','DF','Centro-Oeste')
print(city1.get_nome())