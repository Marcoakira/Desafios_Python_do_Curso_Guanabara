# Desafio088 Esse programa Gera a quantidade solicitada de jogos na loteria
from time import sleep
import random
print(f'{"#"*30}\nBem Vindos ao lotoManiacos\n{"#"*30}')
qJogos = int(input('Quantos Jogos deseja? '))
biglist = []
smallist = []
for c in range(0,qJogos):
    for d in range(0,6):
        a = random.randint(1,60)
        while a in smallist:
            a = random.randint(1,60)
        smallist.append(a)
    smallist.sort()
    biglist.append(smallist[:])
    smallist.clear()


print(f'gerando seu jogo com numeros da sorte !',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')
sleep(1)
for c in range(0,qJogos):
    print(biglist[c])


