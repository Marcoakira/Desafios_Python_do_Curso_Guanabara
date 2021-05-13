# desafio080 esse programa recebe 5 numeros. retorna em ordem crescente sem usar a função sort().

alista = []
alista.append(int(input(f'Insira o 1º Numero ')))
for c in range(1,5):
    nnovo = int(input(f'Insira o {c+1}º Numero '))

    for d in range(0,5):

        if nnovo <= alista[d]:
            alista.insert(d,nnovo)
            break

        if nnovo > alista[-1]:
            alista.append(nnovo)
            break

print(alista)