# Desafio049: fazer a tabuada
num01 = int(input('insira um numero para saber a tabuada dele '))
ate = int(input('insira até onde quer a tabuada '))
for c in range(0,ate):
    number = c+1
    num00 = number*num01
    print(f'{num01} X {number} = {num00}')

