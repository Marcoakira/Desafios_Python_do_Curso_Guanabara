# Desafio051 fazer um sistema de P.A Progressao arentimetrica

nInicial = int(input('Qual o valor inicial? '))
nRazao = int(input('Qual a Razão ? '))
nSquencia =int(input('Qual o tamanha da P.A? '))
sequen = nInicial-nRazao
fim = int(0)
while fim != nSquencia:
        sequen = + nRazao + sequen
        fim += 1
        print(f'fim:{fim}')
        print(sequen)

'''numero inicial
razao
quantos numeros na sequencia

quantas vezes
numero inicial + razao'''