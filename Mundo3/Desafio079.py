# Desafio 079 O programa cria uma lista que recebe varios valores numericos. porem só acrescenta na lista numeros que nao estejam nela.

lunica = []
conti = ('s')




while conti not in 'Nn':
    nnovo = int(input('digite o numero novo :D '))
    # poderia ter usado a expressao:
    # if nnovo not in lunica:
    #   lunica.append(nnovo)
    if lunica.count(nnovo) == 0:
        lunica.append(nnovo)
    else:print('Esse numero ja esta cadastrado, tente outro')
    conti = input('Deseja continuar? S/N')
lunica.sort()
print(lunica)