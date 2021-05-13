

bataTemp = int()
batata  = [[0,0,0],[0,0,0],[0,0,0]]
batataPar = 0
bataSoma = 0
segundabatataMaior = 0
for c in range(0,3):
    for z in range(0,3):
        bataTemp = int(input('Insira o valor: '))
        batata[c][z] = bataTemp
        if bataTemp % 2 == 0:
            batataPar = batataPar + bataTemp
        if z == 2:
            bataSoma += bataTemp
        if z == 1:
            if bataTemp > segundabatataMaior:
                segundabatataMaior = bataTemp

print(f'a soma dos valores pares é {batataPar}')
print(f'A soma dos valores da terceira coluna é {bataSoma}')
print(f' O maior valor da terceira Linha é {segundabatataMaior}')

for c in range (0,3):
    for d in range(0,3):
        print(f'{batata[c][d]:^5}',end='')
    print()

print(batata)