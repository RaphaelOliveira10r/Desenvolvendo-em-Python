class Garrafa:
    def _init_(self,marca,cor,ml):
        self.marca = marca
        self.cor = cor
        self.ml = ml
    
    def _str_(self):
        return self.marca
    
    def get_cor(self):
        return self.cor
    
    def set_garrafa_cor(self,nova):
        self.cor = nova
        


class GarrafaCafe(Garrafa):
    material= 'plastico'
    material_dentro = 'vidro'
    
    def get_garrafa(self,temperatura):
        print(f'A temperatura da garrafa é {temperatura}')
        

class GarrafaJarra(Garrafa):
    material = 'vidro'
    
    def get_garrafa(self,liquido):
        print(f'a garrafa contém {liquido} dentro.')

class GarrafaAgua(Garrafa):
    ...