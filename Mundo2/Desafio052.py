#Desafio052: Le um numero inteiro, e diz se el eé numero primo.
numero = int(input('Digite um numero '))
abacate = 0
for count in range(2,numero):
        if numero % count == 0:
            print(f'esse numero é multiplo de {count}')
            abacate = abacate+1
if abacate == 0:
    print('Esse é um numero primo, pois só é divisivel por 1 e por ele mesmo.')


