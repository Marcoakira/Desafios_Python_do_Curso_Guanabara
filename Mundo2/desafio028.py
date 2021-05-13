#esse programa gera um numero de 0 a 5, pede para o usuario advinhar, e retorna com menssagem de erro ou acerto.

#importa da biblioteca random a função randrange
from random import randrange
from time import sleep
#através da função randrange, atribui um numero aleatorio de 1 até 5 ao naleatorio
nome = input(' Qual o seu nome ?')
moum = ''
if nome[-1] == 'a':
    moum = 'a'
if nome[-1] == 'o':
    moum = 'o'
naleatorio = randrange(1, 5)
sorte =int(input(f'Bom dia meu amig{moum}.\nEstou pensando em um numero de 1 a 5!\nSerá que você acerta? '))
print('Pensando aqui como te trapacear...  ... ...')
sleep(4)
if sorte == naleatorio:
    print(f'parabens você é foda mesmo, é {moum} melh{moum} , só voce é {nome}')
else:
    print(f'Eu tinha pensado em {naleatorio}')
    print(f'{nome} voce nao sabe nada burr{moum} hahahaha \nContinue tentando um dia voce consegue hahahaha!')

if sorte > 5:
    print(f'Você é burro? eu disse de 0 a 5, {sorte} é maior que 5, é cada doido que me aparece.')