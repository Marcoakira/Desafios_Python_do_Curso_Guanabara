# Desafio035: receba os valores de 3 retas e verifica se o mesmo pode formar um triagulo.
r1 = float(input('Qual o tamanho da primeira linha?'))
r2 = float(input('Qual o tamanho da segunda linha?'))
r3 = float(input('Qual o tamanha da terceira linha?'))
s1 = (r2+r3)
s2 = (r1+r3)
s3 = (r1+r2)
if r1 < s1 and r2 < s2 and r3 < s3:
    print('parabens é possivel formar um triangulo com os valores informados')
else: print('Que pena, um dos lados é grande demais para formar um triangulo :(')