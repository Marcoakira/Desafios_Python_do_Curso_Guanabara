# Desafio098 o programa tem uma função que faz a contagem usando as entradas de inicio, fim e passo.
from time import sleep

# funções
def contador(a,b,c):

    print('-='* 21)
    print(f'  contagem de {a} até {b} de {c} em {c}.')
    if a > b:
        c = 0 - c
    if b > 0:
        for cont in range(a,b+1,c):
            print(cont,end=' ')
            sleep(0.5)
        print('... FIM!')
    if b <= 0:
        for cont in range(a, b-1, c):
            print(cont, end=' ')
            sleep(0.5)
        print('... FIM!')



# Código principal

# parte A
ini = int(1)
fim = int(10)
passo = int(1)

contador(ini, fim, passo)

# parte B
ini = int(10)
fim = int(0)
passo = int(2)

contador(ini, fim, passo)


# parte C
print(' Agora é sua vez de personalizar')
ini = int(input('Inicio '))
fim = int(input('Fim '))
passo = int(input('De quanto em Quanto? '))

contador(ini,fim,passo)