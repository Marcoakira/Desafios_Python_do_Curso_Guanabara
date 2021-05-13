# Desafio058c descobrir numero com quente ou frio
from random import randint

numeroPc = randint(0,100)
print(numeroPc)
numeroUser = int()
numerotemp = int()
numerotemp2 = int()
tentativas = int()
while not numeroUser == numeroPc:

    numeroUser = int(input('Advinhe o numero de 0 a 100 que eu estou pensando!'))
    tentativas += 1

    if numeroUser > numeroPc:
        numerotemp = numeroUser - numeroPc
    if numeroUser < numeroPc:
        numerotemp = numeroPc - numeroUser
    print(numerotemp)
    if numerotemp2 < numerotemp:
       print(' ta esfriando')
    if numerotemp2 > numerotemp:
       print(' ta esquentando')

    numerotemp2 = numerotemp
print(f'parabéns voce acertou o numero que eu pensei em {tentativas} tentativas.')