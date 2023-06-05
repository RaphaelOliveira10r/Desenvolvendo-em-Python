# Função de saudação com decoradores e Sintax Suggar 


def saudacao(funcao):
    def saudar():
        print('Bom dia')
        funcao()
        print('Foi um prazer te conhcecer!')
    return saudar

@saudacao # sintax suggar
def outra_saudacao():
    print('Seja bem vindo, aproveite seu dia!')


outra_saudacao()