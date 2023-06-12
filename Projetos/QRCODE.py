import qrcode

dados = input("Digite a informação que deseja gerar o QRCODE: ")

img = qrcode.make(dados)

img.save('Raphael.jpg')