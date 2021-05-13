# Desafio086criar uma matriz 3*3 e preencher ela com dados.
alista =[[],[],[]],[[],[],[]],[[],[],[]]
temp = int()
for c in range(0,3):
    for d in range(0,3):
        temp = int(input(' insira o numero '))
        alista[c][d].append(temp)
print(f'{alista[0]}\n{alista[1]}\n{alista[2]}')
