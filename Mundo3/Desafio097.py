# dasafio097 uma funçao que a moldura do texto acompanha o tamanho do texto

#funçoes
def escreva(msg):
    print('~' * (len(msg)+4))
    print(f'  {msg}')
    print('~' * (len(msg)+4))

#código principal

texto = input('Escreva algo')

escreva(texto)