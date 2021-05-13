#Desafio096 o programa recebe a largura e comprimeto e retorna atraves de uma função a metragem quadrada.

#função que recebe e multiplica 2 valores.
def m2():
    print('¨'*40)
    print('  MEDIDOR MASTER PLUS 2000 DE TERRENOS')

    print('¨' * 40)
    comprimeto = float(input(' insira a o comprimento do terreno: '))
    largura = float(input(' insira a o largura do terreno: '))
    print(f' seu terreno com a metragem {comprimeto} X {largura}tem \033[1:32m{comprimeto*largura} M2\033[m.')


m2()
