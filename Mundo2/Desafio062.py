# Desafio061 feito em while

# Desafio051 fazer um sistema de P.A Progressao arentimetrica

numeroInicial = int(input('Qual valor vai iniciar a sequencia?'))
razao = int(input('Qual a Razão ? '))
tamanhoDaSequencia = (razao * 10) + numeroInicial
controle = int
while controle != 0:
    for conta in range(numeroInicial,tamanhoDaSequencia,razao):
        print(conta)

