#Desafio023. Ao inserir um int de 0 - 9999, ira serpara em unidades, dezenas, centenas, milhar.
num = input('insira um numero de 0 a 9999 com 4 digitos: ')

unidade = num[3]
dezena = num[2]
centena = num[1]
milhar = num[0]

print = (f'A Unidade é {unidade}\nA Dezena é {dezena}\nA Centena é {centena}\nA Milhar é {milhar}')