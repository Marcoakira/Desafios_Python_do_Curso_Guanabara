# Desafio086b criar uma matriz 3*3 e preencher ela com dados.
alista = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        alista[l][c] = int(input(f'Insira o numero da posição {l},{c}'))

for c in range (0,3):
    for d in range(0,3):
        print(f'{alista[c][d]:^5}',end='')
    print()

# print(f'{alista[0]:^5}\n{alista[1]}\n{alista[2]}') # essa é outra posssiblidade de fazer o print
