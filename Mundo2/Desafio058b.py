# Desafio058 melhore o jogo do desafio028, de adivinhar o numero escolhido.

from random import randrange
from time import sleep
#através da função randrange, atribui um numero aleatorio de 1 até 5 ao naleatorio
print('Bom dia Amigo(a), tudo bem?')
naleatorio = randrange(1,100)
sorte = int(222)
tentativa = 0
while sorte != naleatorio:
    naleatorio =
        sorte =int(input('Estou pensando em um numero de 1 a 5!\nSerá que você acerta? '))
    print('Pensando aqui como te trapacear...  ... ...')
    tentativa += 1
    sleep(2)
    if sorte == naleatorio:
        print(f'parabens você é foda mesmo, eu estava pensando em {naleatorio}')
    if sorte != naleatorio and sorte < 6:
        print(f'Eu tinha pensado em {naleatorio}')
        print('Continue tentando um dia voce consegue hahahaha!')
        print('Vamos tentar novamente até voce acertar')

    if sorte > 5:
        print(f'Você é burro? eu disse de 0 a 5')

print(f'voce precisou de {tentativa} tentativas para acertar.')

