#Desafio030: essa aplicação ao receber um numero inteiro, informa ao usuario se o mesmo é par, ou impar.
num = str(input('digite um numero(inteiro)')).strip()
numlen = len(num)
unum = num[numlen-1]
lista = '0 2 4 6 8 '
numr = unum in lista
if True == numr:
    print('seu numero é Par')
else:
    print('seu numero é Ímpar')
