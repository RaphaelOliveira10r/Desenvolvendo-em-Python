# Checa senha com classes


from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha,rounds=1000,salt_size=10)

    def get_nome_completo(self):
        return f'Nome completo: {self.__nome} {self.__sobrenome}'

    def checa_senha(self,senha):
        if cryp.verify(senha,self.__senha):
            return True
        return False
    


while True:
    nome = input('Digite o seu nome:')
    sobrenome = input('Digite o seu sobrenome:')
    email = input('Digite o seu e-mail:')
    senha = input('Digite a sua senha:')
    confirmar_senha = input('Confirme a sua senha:')
    if senha == confirmar_senha:
        user = Usuario(nome,sobrenome,email,senha)
        break
    else:
        print('As senhas não confere!')

print('Usuário criado com sucesso!')


senha = input('informe a senha para acesso:')


if user.checa_senha(senha):
    print('Acesso permitido!')
else:
    print('Acesso negado!')