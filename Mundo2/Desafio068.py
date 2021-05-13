# Desafio068 programa que jogue par ou impar. finaliza quando jogador perder, mostrando total de vitorias consecutivas.

# importanto a função rondom e a funçãi sleep.
from random import randint
import time
numeropc = randint(0,10)
resultadoFinal = str()
resultadoFinalN = int()
imparParPc = int
falaPc = str()
contador = -1
while resultadoFinalN != imparParPc:
    # escolha do jogador
    jogadorPouI = str(input('escolha PAR ou IMPAR ')).strip().lower()
    imparParjogador = int()

    # Escolha do Pc


    # convertemos a string em inteiro
    if jogadorPouI == 'par':
        imparParjogador = 0
        imparParPc = 1
        falaPc = 'IMPAR'
        print(' Você é \033[2;32m PAR \033[m e eu sou \033[2;32m IMPAR \033[m ')
    if jogadorPouI == 'impar':
        imparParjogador = 1
        imparParPc = 0
        falaPc = 'PAR'
        print(' Você é \033[2;32m IMPAR \033[m e eu sou \033[2;32m PAR \033[m ')
    else:
        print('Esse é um jogo de par ou impar, entao digite algo valido, como Par ou Impar')

    print('Estou pensando em um numero...')
    time.sleep(2)
    print('....')
    time.sleep(1)
    print('....... ')
    time.sleep(1)
    print('pronto ja pensei...')
    myescolha = int(input('Sua vez escolha quantos dedos. \nSó valem os das mãos, ou seja, escola de 1 a 10 '))

    contador += 1
    soma = numeropc + myescolha

    if soma %2 == 0:
        resultadoFinal = 'PAR'
        resultadoFinalN = 0
    if soma %2 != 0:
        resultadoFinalN = 1
        resultadoFinal = 'IMPAR'

    if resultadoFinalN == imparParjogador:
        print(f'Eu escolhi {numeropc}, ja voce escolheu {myescolha}, o total é {soma} que é um numero {resultadoFinal}, entao você Ganhou. vamos outra')

print(f'Voce perdeu, mas ganhou {contador} vezes antes de perder.')
