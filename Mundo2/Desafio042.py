# Desafio042: receba os valores de 3 retas e verifica se o mesmo pode formar um triagulo.
r1 = float(input('Qual o tamanho da primeira linha?'))
r2 = float(input('Qual o tamanho da segunda linha?'))
r3 = float(input('Qual o tamanha da terceira linha?'))
s1 = (r2+r3)
s2 = (r1+r3)
s3 = (r1+r2)
if r1 < s1 and r2 < s2 and r3 < s3:
    if r1 == r2 == r3:
        print(' Esse é um Triângulo \033[1:mEquilátero\033[m. Todos os lados são iguais ')
    elif r1 != r2 != r3 != r1:
        print('Esse é um Triângulo \033[1:mEscaleno\033[m. Nenhum dos lados é igual')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r1 == r3 and r1 != r2:
        print('Esse é um Triângulo \033[1:mIsósceles.\033[m Tem dois lados iguais e um diferente.')
else: print('Que pena, um dos lados é grande demais para formar um triangulo :(')