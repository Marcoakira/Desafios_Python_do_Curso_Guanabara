#Desafio102 motra o fatorial e atraves de show=True define se mostra a conta.


def fatorial(n=1,show=False):
    f = 1
    lista = []

    for c in range(n,0,-1):
        f = f * (c )
        lista.append(c)


    if show:
        for x in range(0,len(lista)):
            print(f'{lista[x]}', end='')
            if lista[x] > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')



    return (f)


print(fatorial(5,True))


