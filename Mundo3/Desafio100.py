# Desafio100 o programa vai que tem 2 funçoes, uma sorteia 5 numeros, e a segunda mostra a soma dos numeros pares sorteados.
from time import sleep
from random import randint

def sorteia(five):
    for c in range(0,5):
        five.append(randint(0,10))



def somaPar(par):
    ospares = 0

    print(f'Sorteando... \nOs numeros sorteados foram...')
    print('...',end=' ')
    sleep(1)
    print('..',end=' ')
    sleep(1)
    print('.',end=' ')
    sleep(1)
    for c in range(0,len(par)):
        print(par[c],end=' ')
        if par[c] % 2 == 0:
            ospares += par[c]
    print(f' e a soma dos numeros pares = {ospares}')


numeros = []
sorteia(numeros)
print(numeros)
somaPar(numeros)
