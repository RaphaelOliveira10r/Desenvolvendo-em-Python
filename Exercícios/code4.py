

def num_list(lista,numero):
    for i in enumerate(lista):
        for y in enumerate(numero):
            print(i,y)


letras = ['a','b','c']
numeros= [1,2,3]


(num_list(letras,numeros))